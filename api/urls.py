from django.urls import path, include
from rest_framework import routers

from .views import (CustomerViewSet, MovieViewSet, MovieFileViewSet, ReviewViewSet, SearchMovieViewSet)

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'movie-file', MovieFileViewSet)
router.register(r'review', ReviewViewSet)
# router.register(r'search', SearchMovieViewSet.as_view(), basename='movie search')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', SearchMovieViewSet.as_view(), name='search movie')
]
