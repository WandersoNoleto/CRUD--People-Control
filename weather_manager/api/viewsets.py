import os
import datetime
import requests

from dotenv import load_dotenv
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WeatherRequestSerializer
from statistics import mode

load_dotenv()

class WeatherAPIViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def weather(self, request):
        serializer = WeatherRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        city    = serializer.validated_data.get('city')
        state   = serializer.validated_data.get('state')
        country = serializer.validated_data.get('country')
        info    = request.query_params.get('info', 'full')

        api_key  = os.getenv('OPEN_WHEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state},{country}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if info == 'media':
            numeric_fields = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'sea_level', 'grnd_level', 'humidity', 'temp_kf', 'speed', 'deg', 'gust', 'visibility', 'pop', 'rain_3h']
            numeric_values = {field: [] for field in numeric_fields}

            for item in data['list']:
                if 12 <= int(item['dt_txt'].split()[1].split(':')[0]) <= 18:
                    for field in numeric_fields:
                        if field in item['main']:
                            numeric_values[field].append(item['main'][field])
                        elif field in item['wind']:
                            numeric_values[field].append(item['wind'][field])
                        elif field == 'visibility':
                            numeric_values[field].append(item[field])
                        elif field == 'pop':
                            numeric_values[field].append(item[field])
                        elif 'rain' in item and field == 'rain_3h':
                            if '3h' in item['rain']:
                                numeric_values[field].append(item['rain']['3h'])

            print(numeric_values['temp'])
            averaged_values = {field: sum(values) / len(values) if values else None for field, values in numeric_values.items()}

            non_numeric_fields = ['main', 'description', 'icon', 'pod']
            frequent_values = {}
            for field in non_numeric_fields:
                values = [item['weather'][0][field] for item in data['list'] if 'weather' in item and field in item['weather'][0]]
                if values:
                    frequent_values[field] = mode(values)
                else:
                    frequent_values[field] = None

            single_record = {
                'main': averaged_values,
                'weather': [{
                    'id': None,
                    'main': frequent_values['main'],
                    'description': frequent_values['description'],
                    'icon': frequent_values['icon'],
                }],
                'wind': {
                    'speed': averaged_values['speed'],
                    'deg': averaged_values['deg'],
                    'gust': averaged_values['gust']
                },
                'visibility': averaged_values['visibility'],
                'pop': averaged_values['pop'],
                'rain': {
                    '3h': averaged_values['rain_3h']
                },
            }

            return Response({'data': single_record}, status=status.HTTP_200_OK)

        return Response({'data': data}, status=status.HTTP_200_OK)
