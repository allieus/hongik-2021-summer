from django.db.models.indexes import Index
from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("<int:pk>/mov/", views.movie_detail, name="movie_detail"),
    path("<int:post_pk>/review/new/", views.review_new, name="review_new"),
    path("<int:post_pk>/review/edit/", views.review_edit, name="review_edit"),
    path(
        "<int:post_pk>/review/delete/",
        views.review_delete,
        name="review_delete",
    ),
    # localhost/movie/1/mov/
]
