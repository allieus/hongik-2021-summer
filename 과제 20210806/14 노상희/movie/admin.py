from django.contrib import admin
from movie.models import Actor, Movie, Video, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "photo"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ["actor", "title"]
    list_display = ["actor", "title", "poster", "desc"]
    list_filter = ["title"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["title", "name"]
    list_display = ["title", "name", "youtube_url"]
    list_filter = ["created_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "message"]
