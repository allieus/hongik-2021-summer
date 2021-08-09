from django import forms
from movie.models import Movie, Actor, Review, Video


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # 유저로부터 입력받을 필드 이름들을 나열
        fields = ["title", "actor", "director", "poster", "desc"]


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        # 유저로부터 입력받을 필드 이름들을 나열
        fields = ["name", "photo"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["message"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "youtube_url"]
