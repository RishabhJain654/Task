from django import forms
from .models import Tracks, Genres

class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ('title', 'genre', 'rating',)

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ('name',)
