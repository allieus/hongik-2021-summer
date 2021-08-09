from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path("new/", views.movie_new, name="movie_new"),
    path("<int:pk>/edit/", views.movie_edit, name="movie_edit"),
    path("actor/", views.actor_index, name="actor_index"),
    path("actor/<int:actor_pk>/", views.actor_detail, name="actor_detail"),
    path("<int:post_pk>/reviews/new/", views.Review_new, name="Review_new"),
    path("<int:post_pk>/reviews/<int:pk>/edit/", views.Review_edit, name="Review_edit"),
    path("<int:post_pk>/reviews/<int:pk>/delete/",views.Review_delete,name="Review_delete",),
]