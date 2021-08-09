from django.contrib import admin
from movie.models import Actor, Movie, Video, Review

# Register your models here.
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "photo", "created_at"]
    list_filter = ["created_at"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "poster", "actor", "director", "created_at"]
    list_filter = ["created_at"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["movie"]
    list_display = ["movie", "name", "youtube_url", "created_at"]
    list_filter = ["created_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["movie"]
    list_display = ["movie", "message", "created_at"]
    list_filter = ["created_at"]
