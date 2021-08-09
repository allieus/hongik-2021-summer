from django.urls import path

from movies import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("movie/", views.movie_list, name="movie_list"),
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("movie/<int:movie_pk>/review/new/", views.review_new, name="review_new"),
    path("movie/<int:movie_pk>/review/<int:pk>/edit/", views.review_edit, name="review_edit"),
    # 댓글 삭제
    path(
        "movie/<int:movie_pk>/review/<int:pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
