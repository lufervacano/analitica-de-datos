from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import DentalExamViewSet

router = DefaultRouter()
router.register(r'', DentalExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
