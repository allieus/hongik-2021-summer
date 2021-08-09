from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 상속을 위한 준비/abstract=True를 선언하면 가상의 클래스가 된다.
    class Meta:
        abstract = True


class Book(TimestampModel):
    title = models.CharField(max_length=30, unique=True)
    cover_img = models.ImageField()
    desc = models.TextField()
    writer = models.CharField(max_length=30)
    published_at = models.DateField(blank=True)
    publisher = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Writer(TimestampModel):
    title = models.ForeignKey(Book, on_delete=CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Review(TimestampModel):
    title = models.ForeignKey(Book, on_delete=CASCADE)
    message = models.TextField()


class Video(TimestampModel):
    title = models.ForeignKey(Book, on_delete=CASCADE)
    youtube_url = models.URLField()
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Tag(TimestampModel):
    book = models.CharField(max_length=10)
    tag = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.tag

