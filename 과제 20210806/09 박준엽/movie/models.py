from django.db import models
from django.core.validators import MinLengthValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Movie(TimestampedModel):
    name = models.CharField(max_length=1000)
    poster = models.ImageField()
    director = models.CharField(max_length=50)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name


class Video(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.movie.name


class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.movie.name
