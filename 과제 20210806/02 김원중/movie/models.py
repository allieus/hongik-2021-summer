from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

# create & update 클래스로 다시 묶기


class Actor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="profile_pic", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Video(models.Model):
    # movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    # Movie와 1:N의 관계
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Trailer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.name
