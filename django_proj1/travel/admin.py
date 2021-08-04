from django.contrib import admin

from travel.models import Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "message", "latitude", "longitude"]
