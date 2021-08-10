from django.db import models
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

    def youtube_embed_html(self):
        # https://www.youtube.com/watch?v=xyfozmk1SxQ
        if 'v=' in self.youtube_url:
            youtube_id = self.youtube_url.split('v=')[1]
            html = f"""
                <iframe id="ytplayer" type="text/html" width="640" height="360"
                src="https://www.youtube.com/embed/{youtube_id}?autoplay=1&origin=http://example.com"
                frameborder="0"></iframe>
            """
            return mark_safe(html)
        return None


class Review(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
