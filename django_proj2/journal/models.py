from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Journalist(TimestampedModel):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Post(TimestampedModel):
    journallist = models.ForeignKey(Journalist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message
