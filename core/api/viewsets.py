from rest_framework.viewsets import ModelViewSet

from core.models import TourismSpot

from .serializers import TourismSpotSerializer


class TourismSpotViewSet(ModelViewSet):
    queryset = TourismSpot.objects.all()
    serializer_class = TourismSpotSerializer
    