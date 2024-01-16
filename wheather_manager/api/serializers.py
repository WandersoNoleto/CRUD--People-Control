from rest_framework import serializers


class WeatherRequestSerializer(serializers.Serializer):
    city    = serializers.CharField()
    state   = serializers.CharField()
    country = serializers.CharField()