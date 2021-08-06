from django.urls import path

from journal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    # 댓글 쓰기
    path("<int:post_pk>/comments/new/", views.comment_new, name="comment_new"),
    # 댓글 수정
    path(
        "<int:post_pk>/comments/<int:pk>/edit/", views.comment_edit, name="comment_edit"
    ),
]
