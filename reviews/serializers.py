from rest_framework import serializers
from reviews.models import Review
from movies.models import Movie
from movies.serializers import MovieListDetailSerializer 


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comment', 'movie_title']
    
    def get_movie_title(self, obj):
        # Obtém o objeto do filme associado à avaliação
        movie = Movie.objects.get(pk=obj.movie_id)
        # Serializa o objeto do filme para obter seus dados, incluindo o título
        serializer = MovieListDetailSerializer(movie)
        # Retorna o título do filme
        return serializer.data['title']

