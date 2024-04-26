from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # title = serializers.ReadOnlyField(source='movie.title')
    title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'title', 'stars', 'comment']
    
    def get_title(self, obj):
        title = obj.movie.title
        return title