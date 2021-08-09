from django.db import models

# Create your models here.

from django.contrib.admin.options import csrf_protect_m
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.ForeignKey(Actor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    poster = models.ImageField(blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.title


# 프로모션 유튜브 비디오
class Video(models.Model):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()


class Review(models.Model):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
