from django.contrib import admin

from journal.models import Comment, Journalist, Post

# class JournalistAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Journalist, JournalistAdmin)


@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "ip", "created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
