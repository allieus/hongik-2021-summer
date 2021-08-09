from django.urls import path
from production import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/", views.movie_index, name="movie_index"),
    path("<int:pk>/", views.actor_list_detail, name="actor_list_detail"),
    path("movie/<int:pk>/", views.movie_list_detail, name="movie_list_detail"),
    path("movie/<int:pk>/reviews/new/", views.review_new, name="review_new"),
    path(
        "movie/<int:pk>/reviews/<int:review_pk>/edit/",
        views.review_edit,
        name="review_edit",
    ),
    path(
        "movie/<int:pk>/reviews/<int:review_pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
