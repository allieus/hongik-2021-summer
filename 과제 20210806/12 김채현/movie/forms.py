from django import forms
from movie.models import Actor, Movie, Video, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]


class LinkForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["movie", "youtube_url"]
