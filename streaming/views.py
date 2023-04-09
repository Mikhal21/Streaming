from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from streaming.models import Movie, UserProfile, SubscriptionPlan
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

def user(request, user_id):
    try:
        user = UserProfile.objects.get(pk=user_id)
        return render(request, 'streaming/user.html', {'user': user})
    except ObjectDoesNotExist:
        raise Http404('User not found')

def subscription_plan_movies(request, subscription_id):
    subscription = SubscriptionPlan.objects.get(pk=subscription_id)
    movies = subscription.movies.all()
    return render(request, 'streaming/subscriptions.html', {'subscription': subscription, 'movies': movies})
