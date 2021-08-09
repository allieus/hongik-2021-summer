from django import forms
from movie.models import Actor, Movie, Video, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]
