from django.contrib import admin
from journal.models import Journalist, Post, Comment

# class JournalistAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Journalist, JournalistAdmin)


@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
