from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from spots.models import TouristSpot
from django_filters.rest_framework import DjangoFilterBackend
from spots.serializers import TouristSpotSerializer
from rest_framework import status
from utils.calc_distance import calculate_distance

class TouristSpotViewSet(ModelViewSet):
    queryset         = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    http_method_names  = ['get', 'options', 'head', 'patch', 'post', 'delete']

    @action(detail=False, methods=['get'])
    def nearby(self, request):
        try:
            latitude  = float(request.query_params.get('latitude'))
            longitude = float(request.query_params.get('longitude'))
            radius    = float(request.query_params.get('radius', 10)) 
        except ValueError:
            return Response({'error': 'Latitude, longitude, and radius must be valid float values.'}, status=status.HTTP_400_BAD_REQUEST)

        location = (latitude, longitude)

        nearby_spots = []
        for spot in self.queryset:
            spot_location = (spot.latitude, spot.longitude)
            distance = calculate_distance(location, spot_location)
            if distance <= radius:  
                nearby_spots.append(spot)

        serializer = self.get_serializer(nearby_spots, many=True)
        return Response(serializer.data)