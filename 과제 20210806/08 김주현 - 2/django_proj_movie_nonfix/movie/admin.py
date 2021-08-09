from django.contrib import admin
from movie.models import Actor, Movie, Video, Review

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["actor_name", "poster", "desc"]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["video", "youtube_url"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass