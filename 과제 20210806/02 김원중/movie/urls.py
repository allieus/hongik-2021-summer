from movie.views import index, actor_detail, movie_list, movie_detail
from django.urls import path
from movie import views

urlpatterns = [  # path뒤에 ".../" 슬래시 꼭꼭꼭!!!!!!!적기
    path("", views.index, name="index"),  # views.py에서 indext 함수와 연결함
    path("<int:pk>/", views.actor_detail, name="actor_detail"),
    path("movie/", views.movie_list, name="movie_list"),
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("new/", views.movie_new, name="movie_new"),
    path("movie/<int:pk>/edit/", views.movie_edit, name="movie_edit"),
    path("<int:movie_pk>/review/new/", views.review_new, name="review_new"),
    path(
        "<int:movie_pk>/review/<int:review_pk>/edit/",
        views.review_edit,
        name="review_edit",
    ),
]
