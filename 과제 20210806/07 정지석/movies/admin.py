from movies.models import Actor, Movie, Video, Review
from django.contrib import admin

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]
    search_fields = ["name"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "poster", "desc"]
    search_fields = ["title"]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "youtube_url"]
    search_fields = ["title"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["messages"]