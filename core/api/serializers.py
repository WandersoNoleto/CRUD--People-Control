from rest_framework.serializers import ModelSerializer

from core.models import TourismSpot


class TourismSpotSerializer(ModelSerializer):
    class Meta:
        model = TourismSpot
        fields = ('id', 'name', 'description', 'image')

    