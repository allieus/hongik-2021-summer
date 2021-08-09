from django import forms
from movie.models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["actor_name", "name", "poster", "desc"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]