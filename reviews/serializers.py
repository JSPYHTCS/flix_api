from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')
    class Meta:
        model = Review
        fields = '__all__'
