from rest_framework.serializers import ModelSerializer

from spots.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'image')

    