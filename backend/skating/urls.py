from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkaterViewSet, ElementViewSet, ResultViewSet


router = DefaultRouter()
router.register(r'skaters', SkaterViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'results', ResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
