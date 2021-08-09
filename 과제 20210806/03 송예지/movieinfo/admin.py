from django.contrib import admin

from movieinfo.models import Actor, Movie, Video, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'actor', 'desc']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['movie', 'youtube_url']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'message']
