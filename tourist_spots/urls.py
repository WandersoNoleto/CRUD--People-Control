from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from feedback.api.viewsets import FeedbackViewSet
from spots.api.viewsets import TouristSpotViewSet
from weather_manager.api.viewsets import WeatherAPIViewSet

router = routers.DefaultRouter()
router.register(r'tourist-spots', TouristSpotViewSet, basename='TouristSpot')
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'openWeather', WeatherAPIViewSet,basename="weather-api")



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('spots/', include('spots.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)