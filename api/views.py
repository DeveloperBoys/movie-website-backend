from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, filters
from .serializers import (CustomerSerializer, MovieSerializer, MovieFileSerializer, ReviewSerializer,
                          SearchMovieSerializer)
from .models import (Customer, Movie, MovieFile, Review)


class CustomerViewSet(viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = Customer.objects.create(**serializer.validated_data)
            payload = {
                'success': 'User created successfully',
                'created_obj': obj
            }
            return HttpResponse(payload, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = None
    http_method_names = ['get']


class MovieFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer
    # permission_classes = None
    http_method_names = ['get']


class ReviewViewSet(viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = None
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = Review.objects.create(**serializer.validated_data)
            payload = {
                'success': 'Comment created successfully',
                'created_obj': obj
            }
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchMovieViewSet(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = SearchMovieSerializer
    permission_classes = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
