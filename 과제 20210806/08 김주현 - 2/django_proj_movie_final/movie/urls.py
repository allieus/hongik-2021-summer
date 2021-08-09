from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path("", views.actor_list, name="actor_list"),
    path("new/", views.actor_new, name="actor_new"),
    path("<int:pk>/edit/", views.actor_edit, name="actor_edit"),
    path("<int:pk>/delete/", views.actor_delete, name="actor_delete"),
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("<int:post_pk>/reviews/new/", views.Review_new, name="Review_new"),
    path("<int:post_pk>/reviews/<int:pk>/edit/", views.Review_edit, name="Review_edit"),
    path("<int:post_pk>/reviews/<int:pk>/delete/",views.Review_delete,name="Review_delete"),
    path("<int:pk>/movie/new/", views.movie_new, name="movie_new"),
    path("<int:pk>/movie/<int:post_pk>/edit/", views.movie_edit, name="movie_edit"),
    path("<int:pk>/movie/<int:post_pk>/delete/", views.movie_delete, name="movie_delete"),
]