from django.shortcuts import render
from .models import Movie

# Create your views here.

def list(request):
    movies = Movies.objects.all().order_by('-id')

    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)

