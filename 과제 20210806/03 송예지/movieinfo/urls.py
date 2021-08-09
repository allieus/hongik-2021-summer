from django.urls import path
from movieinfo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movie_list, name="movies_list"),
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("<int:pk>/movies/<int:movie_pk>/",
         views.movie_detail, name="movie_detail"),
    path("actors/new/", views.actor_new, name="actor_new"),
    path("<int:pk>/movies/new/",
         views.movie_new, name="movie_new"),
    path("<int:pk>/movies/<int:movie_pk>/reviews/new/",
         views.review_new, name="review_new"),
    path(
        "<int:pk>/movies/<int:movie_pk>/reviews/<int:review_pk>/edit/", views.review_edit, name="review_edit"
    ),
    path(
        "<int:pk>/movies/<int:movie_pk>/reviews/<int:review_pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
    path("<int:pk>/movies/<int:movie_pk>/videos/new/",
         views.video_new, name="video_new"),

]
