from django.contrib import admin
from movie.models import Actor, Movie, Video, Review
from embed_video.admin import AdminVideoMixin

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "actor", "poster", "desc"]

@admin.register(Video)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ["movie", "youtube_url"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass