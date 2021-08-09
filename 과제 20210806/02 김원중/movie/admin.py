from django.contrib import admin
from movie.models import Actor, Movie, Video, Review, Trailer


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "poster", "desc"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["name", "youtube_url"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["movie", "message"]


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ["movie", "name", "youtube_url"]

