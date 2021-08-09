from django import forms
from movie.models import Movie, Review, Actor

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "actor", "poster", "desc"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["comment"]

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ["name", "photo"]
