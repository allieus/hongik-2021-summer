from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField

# Create your models here.
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(TimestampedModel):
    name = models.CharField(max_length=20)
    photo = models.ImageField()
    # many to many로 Movie와 연결하는 방법 찾아보기

    def __str__(self):
        return self.name


class Movie(TimestampedModel):
    title = models.CharField(max_length=30)
    poster = models.ImageField()
    desc = models.TextField()
    director = models.CharField(max_length=20)
    actor = models.ForeignKey(Actor, on_delete=CASCADE)

    def __str__(self):
        return self.title


class Video(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_url = models.URLField()

    def __str__(self):
        return self.name


class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    message = models.TextField()

