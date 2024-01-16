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
    
    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).partial_update(request, *args, **kwargs)