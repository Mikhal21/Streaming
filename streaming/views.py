from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404
from streaming.models import Movie
from django.db.models import Avg

# Create your views here.
def index(request):
    movies_with_avg_rating = Movie.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    return render(request, 'streaming/index.html', {'movies': movies_with_avg_rating})

def movie(request, movie_id):
    try:
        print(Movie.objects.get(pk=movie_id))
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'streaming/movie.html', {'movie': movie})
    except ObjectDoesNotExist:
        raise Http404('Movie not found')
