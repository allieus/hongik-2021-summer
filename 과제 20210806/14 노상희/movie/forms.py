from django import forms
from movie.models import Actor, Movie, Video, Review


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        # 유저로부터 입력 받을 필드 이름들을 나열
        fields = ["name", "photo"]


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["actor", "title", "poster", "desc"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "name", "youtube_url"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "message"]
