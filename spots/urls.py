from django.urls import path

from spots import views
from rest_framework import routers

app_name='spots'

router_spots = routers.SimpleRouter()
router_spots.register('spots', views.TouristSpotViewSet)
print(router_spots.urls)

urlpatterns = [
    path('spots/nearby/', views.TouristSpotViewSet.as_view({'get': 'nearby'}), name='touristspot-nearby'),
]

urlpatterns += router_spots.urls