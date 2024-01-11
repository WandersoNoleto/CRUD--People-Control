from rest_framework.viewsets import ModelViewSet

from spots.models import TourismSpot

from .serializers import TourismSpotSerializer


class TourismSpotViewSet(ModelViewSet):
    serializer_class = TourismSpotSerializer
    
    def get_queryset(self):
        id          = self.request.query_params.get('id', None)
        name        = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset    = TourismSpot.objects.all()

        if id:
            queryset = TourismSpot.objects.filter(pk=id)
        if name:
            queryset.filter(name=name)
        if description:
            queryset.filter(description=description)

        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TourismSpotViewSet, self).partial_update(request, *args, **kwargs)