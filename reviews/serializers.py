# from rest_framework import serializers
# from reviews.models import Review


# class ReviewSerializer(serializers.ModelSerializer):
#     # movie_title = serializers.ReadOnlyField(source='movie.title')

#     class Meta:
#         model = Review
#         # exclude = ['movie']
        
from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Review
        fields = ['id', 'stars', 'comment', 'movie_title']
