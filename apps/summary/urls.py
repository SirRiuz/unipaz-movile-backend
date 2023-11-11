# Django
from django.urls import path, include
from rest_framework import routers

# Views
from apps.summary.views.summary_viewset import SummaryViewSet


router = routers.DefaultRouter()
router.register(r"summary", SummaryViewSet, basename="summary")

urlpatterns = (
    path("", include(router.urls)),
)
