from django.core.checks import messages
from django.db import models
from django.db.models.fields import TextField

class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    poster = models.ImageField()
    desc = TextField()

    def __str__(self) -> str:
        return self.title

class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    messages = models.TextField()
