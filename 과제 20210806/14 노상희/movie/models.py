from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(TimestampedModel):
    name = models.CharField(max_length=20)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Movie(TimestampedModel):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    poster = models.ImageField()
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title


class Video(TimestampedModel):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.youtube_url


class Review(TimestampedModel):
    name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
