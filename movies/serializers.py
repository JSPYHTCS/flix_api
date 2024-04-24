from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from reviews.serializers import ReviewSerializer 


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # reviews = obj.reviews.all()
    # if reviews:
    #   sum_reviews = 0
    #   for review in reviews:
    #     sum_reviews += review.stars
    #   reviews_count = reviews.count()
    #   return round(sum_reviews / reviews_count, 1)
    # return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)  # Campo calculado. Um campo que é só para ser lido e não tem no DB, só na resposta.
    reviews = ReviewSerializer(many=True)  # Inclua o serializer da avaliação

    movie_title = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
