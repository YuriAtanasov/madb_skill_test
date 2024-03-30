from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


GENRE_CHOICES = (
    ('Action', 'ACTION'),
    ('Drama', 'DRAMA'),
    ('Comedy', 'COMEDY'),
    ('Romance', 'ROMANCE'),
)

USER_RATING = (
    ('Recently Added', 'RECENTLY ADDED'),
    ('Most watched', 'MOST_WATCHED'),
    ('Top rated', 'TOP_RATED'),
)


class moviesCatalog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="images/movies/")
    genre = models.CharField(choices=GENRE_CHOICES, max_length=7)
    releaseDate = models.IntegerField()
    director = models.CharField(max_length=50, blank=True)
    userRating = models.CharField(choices=USER_RATING, max_length=14, blank=True)
    viewsCount = models.IntegerField(default=0, blank=True)
    trailerLink = models.CharField(default="", max_length=200, blank=True)
    movieSummary = models.TextField(max_length=10000, default="", blank=True)
    movieSynopsis = models.TextField(max_length=20000, default="", blank=True)

    def __str__(self):
        return self.title


class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(moviesCatalog, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Favorite Movie")
        verbose_name_plural = _("Favorite Movies")

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.movie.title}"
