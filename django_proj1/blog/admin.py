from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    list_display_links = ["title"]
    # list_editable = ["title"]
    search_fields = ["title"]
