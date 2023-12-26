from rest_framework.serializers import ModelSerializer

from tourist_resources.models import Resourse


class ResourseSerializer(ModelSerializer):
    class Meta:
        model = Resourse
        fields = ('id', 'name', 'description', 'operating_hours', 'age_required')
