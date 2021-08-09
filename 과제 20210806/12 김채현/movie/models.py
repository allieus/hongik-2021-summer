from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(null=True, max_length=30)
    name = models.ForeignKey(Actor, on_delete=models.CASCADE)
    poster = models.ImageField(blank=True)
    text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.movie

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()


# Create your models here.
