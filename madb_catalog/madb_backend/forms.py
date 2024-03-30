from django.forms import ModelForm
from django import forms
from .models import moviesCatalog


class UploadForm(ModelForm):
    description = forms.TextInput()
    image = forms.ImageField()
    genre = forms.Select()
    releaseDate = forms.NumberInput()
    director = forms.TextInput()
    userRating = forms.Select()
    viewsCount = forms.NumberInput()
    trailerLink = forms.TextInput()
    movieSummary = forms.TextInput()
    movieSynopsis = forms.TextInput()

    class Meta:
        model = moviesCatalog
        fields = ['title', 'description', 'image', 'genre', 'releaseDate', 'director', 'userRating', 'viewsCount', 'trailerLink', 'movieSummary', 'movieSynopsis']
    title = forms.TextInput()
