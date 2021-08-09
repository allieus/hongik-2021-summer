from django.contrib import admin

# from django.contrib.admin.options import ModelAdmin
from movie.models import Actor, Movie, Video, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "poster", "text"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["message"]
