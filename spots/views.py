from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from spots.models import TouristSpot

from spots.serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    
    def get_queryset(self):
        id          = self.request.query_params.get('id', None)
        name        = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset    = TouristSpot.objects.all()

        if id:
            queryset = TouristSpot.objects.filter(pk=id)
        if name:
            queryset.filter(name=name)
        if description:
            queryset.filter(description=description)

        return queryset
    