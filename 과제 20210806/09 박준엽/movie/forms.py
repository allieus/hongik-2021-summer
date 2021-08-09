from django import forms
from movie.models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # 유저로부터 입력받을 필드들의 이름을 나열
        fields = ["name", "desc", "poster", "director", "actor"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # 유저로부터 입력받을 필드들의 이름을 나열
        fields = ["message"]
