from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from feedback.api.viewsets import FeedbackViewSet
from spots.api.viewsets import TourismSpotViewSet

router = routers.DefaultRouter()
router.register(r'tourismspots', TourismSpotViewSet, basename='TourismSpot')
router.register(r'feedbacks', FeedbackViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)