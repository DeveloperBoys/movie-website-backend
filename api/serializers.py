from rest_framework import serializers

from .models import (Customer, Movie, MovieFile, Review)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'category', 'language', 'date_of_manufacture', 'duration', 'likes']


class MovieFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = ['movie', 'video_url', 'image_url']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'movie', 'title', 'review', 'created_at']
