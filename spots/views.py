from rest_framework.viewsets import ModelViewSet

from spots.models import TouristSpot
from django_filters.rest_framework import DjangoFilterBackend
from spots.serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    queryset         = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']
        