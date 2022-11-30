from django.urls import path, include
from rest_framework import routers

from .views import (CustomerViewSet, MovieViewSet, MovieFileViewSet, ReviewViewSet)

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'movie-file', MovieFileViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
