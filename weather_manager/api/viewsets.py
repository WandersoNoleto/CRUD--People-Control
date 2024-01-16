import os

import requests
from dotenv import load_dotenv
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WeatherRequestSerializer

load_dotenv()

class WeatherAPIViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def weather(self, request):
        serializer = WeatherRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        city    = serializer.validated_data.get('city')
        state   = serializer.validated_data.get('state')
        country = serializer.validated_data.get('country')

        api_key  = os.getenv('OPEN_WHEATHER_API_KEY')
        url      = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state},{country}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        return Response({'data': data}, status=status.HTTP_200_OK)

