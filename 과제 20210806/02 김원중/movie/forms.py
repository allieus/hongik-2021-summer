from django import forms
from django.db.models import fields
from movie.models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["name", "poster", "desc"]  # 유저로부터 입력받을 필드 이름들을 나열


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["movie", "message"]
