from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkaterViewSet, ElementViewSet, ResultViewSet


router = DefaultRouter()
router.register(r'skaters', SkaterViewSet, basename='skater')
router.register(r'elements', ElementViewSet, basename='element')
router.register(r'results', ResultViewSet, basename='result')


urlpatterns = [
    path('', include(router.urls)),
]
