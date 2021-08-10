from django.urls import path
from movie import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path("new/", views.movie_new, name="movie_new"),
    # path("actor/int:actor_pk/", views.actor_detail, name="actor_detail"),
    path("actor/", views.actor_index, name="actor_index"),
]
