from django.db import models
from embed_video.fields import EmbedVideoField

class Actor(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    poster = models.ImageField(blank=True)
    desc = models.TextField()
    def __str__(self) -> str:
        return self.title

class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = EmbedVideoField()

class TimestampedModel(models.Model):
    class Meta:
        abstract = True

class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment