from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def directors(request):
    if request.method == "GET":
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        name = request.data.get('name')
        Director.objects.create(
            name=name
        )
        return Response()





@api_view(['GET', 'POST'])
def movies(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response()





@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        return Response()



@api_view(["GET", "PUT", "DELETE"])
def director_item(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data)







@api_view(["GET"])
def movie_item(request, id):
    try:
         movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        title.save()
        description.save()
        duration.save()
        director_id.save()
        return Response(data=MovieSerializer(movie).data)






@api_view(["GET"])
def review_item(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        text.save()
        stars.save()
        movie_id.save()
        return Response(data=ReviewSerializer(review).data)








