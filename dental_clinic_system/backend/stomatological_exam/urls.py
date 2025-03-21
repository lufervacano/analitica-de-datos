from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import StomatologicalExamViewSet

router = DefaultRouter()
router.register(r'', StomatologicalExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
