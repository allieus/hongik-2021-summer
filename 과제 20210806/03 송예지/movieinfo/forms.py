from django import forms
from django.db.models import fields
from movieinfo.models import Actor, Movie, Video, Review


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        # 유저로부터 입력받을 필드의 이름을 나열
        fields = ['name', 'photo']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # 유저로부터 입력받을 필드의 이름을 나열
        fields = ['title', 'actor', 'poster', 'desc']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['movie', 'youtube_url']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # 유저로부터 입력받을 필드의 이름을 나열
        fields = ['message']
