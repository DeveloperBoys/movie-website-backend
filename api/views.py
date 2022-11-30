from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import (CustomerSerializer, MovieSerializer, MovieFileSerializer, ReviewSerializer)
from .models import (Customer, Movie, MovieFile, Review)


class CustomerViewSet(viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = None
    http_method_names = ['get', 'post']

    # def list(self, request, *args, **kwargs):
    #     username = self.queryset.username
    #     image = self.queryset.image_url
    #     email = self.queryset.email
    #     payload = {
    #         'username': username,
    #         'image': image,
    #         'email': email
    #     }
    #
    #     return Response(payload)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = Customer.objects.create(**serializer.validated_data)
            payload = {
                'success': 'User is create successfully',
                'created_obj': obj
            }
            return Response(payload, status=status.HTTP_201_CREATED)
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
    permission_classes = None
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = Review.objects.create(**serializer.validated_data)
            payload = {
                'success': 'Comment is create successfully',
                'created_obj': obj
            }
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
