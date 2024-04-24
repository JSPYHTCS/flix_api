# from rest_framework import serializers
# from reviews.models import Review


# class ReviewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = '__all__'

from rest_framework import serializers
from reviews.models import Review
from movies.models import Movie

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_movie_title(self, obj):
        movie_id = obj.movie_id
        movie = Movie.objects.filter(id=movie_id).first()
        if movie:
            return movie.title
        else:
            return None
