from django.contrib import admin
from production import models
from production.models import Actor, Movie, Review, Video

# Register your models here.


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "poster", "desc"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "youtube_url"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "message"]
