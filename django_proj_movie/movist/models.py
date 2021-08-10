from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 주연배우
class Actor(TimestampedModel):
    name = models.CharField(max_length=10, db_index=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "주연배우"
        verbose_name_plural = "주연배우 목록"


class Movie(TimestampedModel):
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, verbose_name="주연배우")
    name = models.CharField(max_length=100)
    poster = models.ImageField(verbose_name="포스터 이미지")
    desc = models.TextField(verbose_name="설명")

    def __str__(self) -> str:
        return self.name


class Video(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()

    # 인자없는 멤버함수는 속성처럼 사용하고 싶습니다.
    @property
    def youtube_id(self):
        # https://www.youtube.com/watch?v=xyfozmk1SxQ
        if 'v=' in self.youtube_url:
            return self.youtube_url.split('v=')[1]
        return None

    @property
    def youtube_embed_html(self):
        if self.youtube_id:
            return render_to_string("movist/_youtube_embed.html", {
                "youtube_id": self.youtube_id,
            })
        return None


class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
