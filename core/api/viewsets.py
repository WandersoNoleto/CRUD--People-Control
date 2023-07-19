from rest_framework.viewsets import ModelViewSet

from core.models import TourismSpot

from .serializers import TourismSpotSerializer


class TourismSpotViewSet(ModelViewSet):
    serializer_class = TourismSpotSerializer
    
    def get_queryset(self):
        return TourismSpot.objects.filter(approved=True)