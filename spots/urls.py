from django.urls import path

from spots import views
from rest_framework import routers

app_name='spots'

router_spots = routers.SimpleRouter()
router_spots.register('', views.TouristSpotViewSet, basename='spots')


urlpatterns = router_spots.urls