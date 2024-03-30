from django.urls import path
from .views import MovieLists, BaseTemplate, AboutTemplate
from . import views

app_name = 'madb_backend'

urlpatterns = [
    path('', BaseTemplate.as_view(), name='base_template'),
    path('catalog/', MovieLists.as_view(), name='movie_list'),
    path('catalog/<int:pk>/', views.movdt, name='movie_detail'),
    path('about', AboutTemplate.as_view(), name='about_me'),
    path('catalog/form_base', views.movlst, name='form_base'),
    path('catalog/upload/', views.movadd, name='upload'),
    path('catalog/search/', views.movsrch, name='search'),
    path('catalog/favorites/', views.favorite_movies, name='favorites'),
    path('catalog/favorites/add/<int:movie_id>/', views.add_favorite_movie, name='add_favorite_movie'),
    path('catalog/favorites/remove/<int:favorite_movie_id>/', views.remove_favorite_movie, name='remove_favorite_movie'),
    path('catalog/top-rated/', views.top_rated_movies, name='top_rated'),
    path('catalog/most-watched/', views.most_watched_movies, name='most_watched'),
    path('catalog/recently-added/', views.recently_added_movies, name='recently_added'),
    ]
