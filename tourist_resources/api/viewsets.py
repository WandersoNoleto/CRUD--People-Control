from rest_framework.viewsets import ModelViewSet

from tourist_resources.models import Resourse

from .serializers import ResourseSerializer


class ResourseViewSet(ModelViewSet):
    queryset = Resourse.objects.all()
    serializer_class = ResourseSerializer
    