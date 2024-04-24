from rest_framework import serializers
from reviews.models import Review
from movies.serializers import MovieListDetailSerializer


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListDetailSerializer()

    class Meta:
        model = Review
        fields = '__all__'

