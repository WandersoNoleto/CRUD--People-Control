from django.urls import path

from spots import views
from rest_framework import routers

app_name='tourist-spots'

router_spots = routers.SimpleRouter()
router_spots.register('tourist-spots', views.TouristSpotViewSet)


urlpatterns = [    
    path('tourist-spots/nearby/', views.TouristSpotViewSet.as_view({'get': 'nearby'}), name='touristspot-nearby'),
    path('tourist-spots/weather/<int:id>/', views.TouristSpotViewSet.as_view({'get': 'weather'}), name='touristspot-weather'),
    path('tourist-spots/weather-5/<int:id>/', views.TouristSpotViewSet.as_view({'get': 'weather_5'}), name='touristspot-weather-5'),
    path('tourist-spots/weather-5-summary/<int:id>/', views.TouristSpotViewSet.as_view({'get': 'weather_5_summary'}), name='touristspot-weather-5-summary'),

]

urlpatterns += router_spots.urls