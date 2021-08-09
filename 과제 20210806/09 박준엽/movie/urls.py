from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path("new/", views.movie_new, name="movie_new"),
    path("<int:pk>/edit/", views.movie_edit, name="movie_edit"),
    path("<int:movie_pk>/review/new/", views.review_new, name="review_new"),
    path(
        "<int:movie_pk>/review/<int:pk>/edit/", views.review_edit, name="review_edit",
    ),
    path(
        "<int:movie_pk>/review/<int:pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
    path("<int:pk>/actor/", views.actor_list, name="actor_list"),
]
