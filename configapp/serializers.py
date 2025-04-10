from rest_framework import serializers
from configapp.models import Movie, Actors, CommitMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
    # author = serializers.IntegerField(read_only=True)
    class Meta:
        model = CommitMovie
        fields = ['id', 'title', 'movie','author']


