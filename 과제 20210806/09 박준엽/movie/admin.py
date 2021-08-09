from django.contrib import admin
from movie.models import Actor, Movie, Video, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ["search"]
    list_display = ["name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ["search"]
    list_display = ["name", "director", "actor"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["search"]
    list_display = ["movie", "youtube_url"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["movie", "message"]
