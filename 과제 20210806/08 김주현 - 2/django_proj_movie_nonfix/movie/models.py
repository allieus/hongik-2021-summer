from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        abstract = True  # Name이라는 이름의 테이블이 생성되지 않도록한다.
    def __str__(self) -> str:
        return self.name

class Actor(Name):
    photo = models.ImageField(blank=True)

class Movie(Name):
    actor_name = models.ForeignKey(Actor, on_delete=models.CASCADE)
    poster = models.ImageField(blank=True)
    desc = models.TextField()

class Video(Name):
    video = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()

class TimestampedModel(models.Model):
    class Meta:
        abstract = True

class Review(TimestampedModel):
    post = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message