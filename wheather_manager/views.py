import os

import requests
from django.shortcuts import render
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.views import APIView

from .api.serializers import WeatherRequestSerializer

load_dotenv()

class WeatherAPIView(APIView):
    def get(self, request):
        serializer = WeatherRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        city    = serializer.validated_data.get('city')
        state   = serializer.validated_data.get('state')
        country = serializer.validated_data.get('country')

        api_key  = os.getenv('OPEN_WHEATHER_API_KEY')
        url      = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state},{country}&appid={api_key}'
        response = requests.get(url)
        data     = response.json()

        return Response(data)
