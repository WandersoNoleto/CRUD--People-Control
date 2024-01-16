from django.urls import path

from spots.api.viewsets import TouristSpotViewSet

urlpatterns = [
    path('by-city', TouristSpotViewSet.as_view({'get': 'list_by_city'}), name='tourist-spot-list-by-city'),
    path('by-state', TouristSpotViewSet.as_view({'get': 'list_by_state'}), name='tourist-spot-list-by-state'),
    path('by-country', TouristSpotViewSet.as_view({'get': 'list_by_country'}), name='tourist-spot-list-by-country'),
]
