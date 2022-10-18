from movie_app.models import Director, Review, Movie
from rest_framework import serializers





class DirectorSerializer(serializers.ModelSerializer):
    # title = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'title description duration director reviews rating'.split()



