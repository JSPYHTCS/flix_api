from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    name_movie = serializers.CharField(source='movie.title')

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comment', 'name_movie']
