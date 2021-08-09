from django.contrib import admin
from book.models import Book, Writer, Video, Tag, Review

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "writer", "publisher", "published_at"]
    list_filter = ["title", "writer", "published_at"]


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["title", "name"]
    list_filter = ["title", "name"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "youtube_url"]
    list_filter = ["title"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "message", "created_at", "updated_at"]
    list_filter = ["title", "created_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["tag"]
    list_filter = ["tag"]
