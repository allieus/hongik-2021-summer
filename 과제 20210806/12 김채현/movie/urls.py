from django.db.models.indexes import Index
from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("<int:pk>/mov/", views.movie_detail, name="movie_detail"),
    path("<int:movie_pk>/mov/review/new/", views.review_new, name="review_new"),
    path("<int:movie_pk>/mov/review/edit/",views.review_edit, name="review_edit"),
    #path("<int:movie_pk>/mov/review/<int:review_pk>/edit/",
    # views.review_edit, name="review_edit"),
    #path(
    path(
        "<int:movie_pk>/mov/<int:pk>/videos/new/", views.video_new, name="video_new"
    ),]