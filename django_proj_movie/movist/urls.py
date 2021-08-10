from django.urls import path

from movist import views

urlpatterns = [
    path("actors/", views.actor_list, name="actor_list"),
    path("actors/<int:pk>/", views.actor_detail, name="actor_detail"),
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("movies/<int:movie_pk>/reviews/", views.review_list, name="review_list"),
    path("movies/<int:movie_pk>/reviews/new/",
         views.review_new, name="review_new"),
    path("movies/<int:movie_pk>/reviews/<int:pk>/edit/",
         views.review_edit, name="review_edit"),
    path("movies/<int:movie_pk>/reviews/<int:pk>/delete/",
         views.review_delete, name="review_delete"),
]
