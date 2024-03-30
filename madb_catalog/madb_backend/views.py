from django.views.generic import ListView, TemplateView
from .models import moviesCatalog
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from .models import FavoriteMovie
from django.contrib import messages


# Section for Classes handling views for movie catalog
# -------------------------------------------
class BaseTemplate(TemplateView):
    model = moviesCatalog
    template_name = 'movie_catalog/pages/base.html'
    context_object_name = 'base_template'


class MovieLists(ListView):
    model = moviesCatalog
    template_name = 'movie_catalog/pages/movie_list.html'
    context_object_name = 'movie_list'


class AboutTemplate(TemplateView):
    model = moviesCatalog
    template_name = 'movie_catalog/pages/about_me.html'
    context_object_name = 'about_me'
# -------------------------------------------


# Function displaying movie details
# ---------------------------
def movdt(request, pk):
    movie = get_object_or_404(moviesCatalog, pk=pk)
    return render(request, 'movie_catalog/pages/movie_detail.html', {'movie': movie})


# Functions handling search results for movies
# ---------------------------
def movsrch(request):
    query = request.GET.get('q')
    search_type = request.GET.get('search_type')

    results = []
    if query:
        if search_type == 'title':
            results = moviesCatalog.objects.filter(title__icontains=query)
        elif search_type == 'genre':
            results = moviesCatalog.objects.filter(genre__icontains=query)

    return render(request, 'clients/search_result.html', {'query': query, 'search_type': search_type, 'results': results})


# Section with functions handling movie upload in movie catalog
# -------------------------------------------
def movlst(request):
    movies_list = moviesCatalog.objects.all()
    context = {"avail_movies": movies_list}
    return render(request, "clients/form_base.html", context)


@login_required
def movadd(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/catalog/form_base')
    return render(request, "clients/add_movies.html", {'form': UploadForm})
# -------------------------------------------


# Section with functions handling favorite options for users
# -------------------------------------------
@login_required
def favorite_movies(request):
    favorite_movies = FavoriteMovie.objects.filter(user=request.user)
    return render(request, 'clients/favorite_movies.html', {'favorite_movies': favorite_movies})


@login_required
def add_favorite_movie(request, movie_id):
    if request.method == 'POST':
        # Check if the movie is already in favorites
        movie = get_object_or_404(moviesCatalog, pk=movie_id)
        if FavoriteMovie.objects.filter(user=request.user, movie=movie).exists():
            # Movie is already marked as favorite
            print("Movie is already marked as favorite")  # console print
            messages.info(request, "Movie is already marked as favorite")
            return redirect('/catalog/favorites/', movie_id=movie_id)
        else:
            FavoriteMovie.objects.create(user=request.user, movie=movie)
            print("Movie added to favorites")  # console print
            messages.success(request, "Movie added to favorites")
        return redirect('/catalog/favorites/')
    else:
        return redirect('/catalog/')


@login_required
def remove_favorite_movie(request, favorite_movie_id):
    favorite_movie = get_object_or_404(FavoriteMovie, pk=favorite_movie_id, user=request.user)
    favorite_movie.delete()
    print("Movie removed from favorites")
    return redirect('/catalog/favorites/')
# -------------------------------------------


# Section with functions handling statistics for top rated, most watched and recently added movies
# -------------------------------------------
def top_rated_movies(request):
    top_rated = moviesCatalog.objects.order_by('-userRating')[:5]
    return render(request, 'stats/top_rated.html', {'movies': top_rated})


def most_watched_movies(request):
    most_watched = moviesCatalog.objects.order_by('-viewsCount')[:5]
    return render(request, 'stats/most_watched.html', {'movies': most_watched})


def recently_added_movies(request):
    recently_added = moviesCatalog.objects.order_by('-releaseDate')[:5]
    return render(request, 'stats/recently_added.html', {'movies': recently_added})
# -------------------------------------------
