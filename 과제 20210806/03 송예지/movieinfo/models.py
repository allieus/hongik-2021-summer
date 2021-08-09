from django.db import models
from django.db.models.deletion import CASCADE


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(TimestampedModel):
    name = models.CharField(max_length=20)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Movie(TimestampedModel):
    title = models.CharField(max_length=30)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    poster = models.ImageField()
    desc = models.TextField()

    def __str__(self):
        return self.title


class Video(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()


class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    message = models.TextField()
