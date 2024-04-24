from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)  # Campo para o título do filme

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comment', 'movie_title']
