from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from spots.models import TouristSpot

from .serializers import TouristSpotSerializer


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
    
    @action(detail=False, methods=['GET'])
    def list_by_city(self, request, *args, **kwargs):
        city = self.request.query_params.get('city', None)
        if not city:
            return Response({'error': 'City parameter is required'}, status=400)

        queryset   = TouristSpot.objects.filter(city__iexact=city)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def list_by_state(self, request, *args, **kwargs):
        state = self.request.query_params.get('state', None)
        if not state:
            return Response({'error': 'State parameter is required'}, status=400)

        queryset   = TouristSpot.objects.filter(state__iexact=state)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def list_by_country(self, request, *args, **kwargs):
        country = self.request.query_params.get('country', None)
        if not country:
            return Response({'error': 'Country parameter is required'}, status=400)

        queryset   = TouristSpot.objects.filter(country__iexact=country)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)