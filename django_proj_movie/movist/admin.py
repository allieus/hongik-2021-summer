from django.contrib import admin
from django.utils.safestring import mark_safe

from movist.models import Actor, Movie, Review, Video


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'actor', 'poster_image', 'desc']

    # 적절히 썸네일처리해주면, 페이지가 좀 더 빨리 뜨고, 서버 부담도 줄어든다.
    def poster_image(self, movie: Movie):
        html = f'<img src="{movie.poster.url}" style="width: 100px;" />'
        return mark_safe(html)
    poster_image.short_description = "포스터 이미지"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['movie', 'title', 'youtube_link']

    def youtube_link(self, video: Video) -> str:
        html = f'<a href="{video.youtube_url}" target="_blank">바로보기</a>'
        return mark_safe(html)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
