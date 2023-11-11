# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from apps.califications.views.calification_viewset import CalificationViewSet

router = DefaultRouter()
router.register(r'califications', CalificationViewSet, basename="califications")


urlpatterns = [
    path('', include(router.urls)),
]
