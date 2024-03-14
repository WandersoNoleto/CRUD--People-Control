from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from spots.models import TouristSpot
from django_filters.rest_framework import DjangoFilterBackend
from spots.serializers import TouristSpotSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from utils.calc_distance import calculate_distance
import os
import requests
from collections import Counter
import statistics

class TouristSpotViewSet(ModelViewSet):
    queryset         = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'city', 'state', 'country']
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']

    @action(detail=False, methods=['get'])
    def nearby(self, request):
        try:
            latitude  = float(request.query_params.get('latitude'))
            longitude = float(request.query_params.get('longitude'))
            radius    = float(request.query_params.get('radius', 10)) 
        except ValueError:
            return Response({'error': 'Latitude, longitude, and radius must be valid float values.'}, status=status.HTTP_400_BAD_REQUEST)

        location = (latitude, longitude)

        nearby_spots = []
        for spot in self.queryset:
            spot_location = (spot.latitude, spot.longitude)
            distance = calculate_distance(location, spot_location)
            if distance <= radius:  
                nearby_spots.append(spot)

        serializer = self.get_serializer(nearby_spots, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def weather(self, request, id=None):
        try:
            tourist_spot = get_object_or_404(TouristSpot, id=id)
            latitude     = tourist_spot.latitude
            longitude    = tourist_spot.longitude
            
            ow_key = os.environ.get('OPEN_WEATHER_API_KEY')
            url    = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={ow_key}&units=metric'
            
            response = requests.get(url)
            data     = response.json()
            
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def weather_5(self, request, id=None):
        try:
            tourist_spot = get_object_or_404(TouristSpot, id=id)
            latitude     = tourist_spot.latitude
            longitude    = tourist_spot.longitude
            
            ow_key = os.environ.get('OPEN_WEATHER_API_KEY')
            url    = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={ow_key}&units=metric'
            
            response = requests.get(url)
            data     = response.json()
            
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])    
    def weather_5_summary(self, request, id=None):
        try:
            tourist_spot = get_object_or_404(TouristSpot, id=id)
            latitude     = tourist_spot.latitude
            longitude    = tourist_spot.longitude
            
            ow_key = os.environ.get('OPEN_WEATHER_API_KEY')
            url    = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={ow_key}&units=metric'
            
            response = requests.get(url)
            data     = response.json()
            
            weather_data = data['list']

            temperatures   = [item['main']['temp'] for item in weather_data]
            avg_temp       = statistics.mean(temperatures)
            feels_like     = [item['main']['feels_like'] for item in weather_data]
            avg_feels_like = statistics.mean(feels_like)
            pressures      = [item['main']['pressure'] for item in weather_data]
            avg_pressure   = statistics.mean(pressures)
            humidities     = [item['main']['humidity'] for item in weather_data]
            avg_humidity   = statistics.mean(humidities)
            descriptions   = [item['weather'][0]['description'] for item in weather_data]
            most_common_description = Counter(descriptions).most_common(1)[0][0]
            
            weather_summary = {
                'cod': 200,
                'coord': {'lat': latitude, 'lon': longitude},
                'weather': {
                    'avg_temp': avg_temp,
                    'avg_feels_like': avg_feels_like,
                    'avg_pressure': avg_pressure,
                    'avg_humidity': avg_humidity,
                    'most_common_description': most_common_description
                }
            }

            return Response(weather_summary, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)