from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.api.viewsets import TourismSpotViewSet

router = routers.DefaultRouter()
router.register(r'tourismspot', TourismSpotViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
