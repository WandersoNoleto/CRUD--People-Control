from rest_framework.serializers import ModelSerializer

from location.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'address', 'complement', 'city', 'region', 'country', 'latitude', 'longitude')


