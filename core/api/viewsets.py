from rest_framework.viewsets import ModelViewSet

from core.models import TourismSpot

from .serializers import TourismSpotSerializer


class TourismSpotViewSet(ModelViewSet):
    serializer_class = TourismSpotSerializer
    
    def get_queryset(self):
        return TourismSpot.objects.filter(approved=True)
    
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