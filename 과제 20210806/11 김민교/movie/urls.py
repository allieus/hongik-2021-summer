from movie import views
from django.urls import path

urlpatterns = [
    # 메인 화면 영화 리스트
    path("", views.index, name="index"),
    # 영화 디테일 연결
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    # 배우 리스트
    path("actor/", views.actor_index, name="actor_index"),
    # 배우 디테일 연결
    path("actor/<int:actor_pk>/", views.actor_detail, name="actor_detail"),
    # 배우 추가
    path("actor/new/", views.actor_new, name="actor_new"),
    # 영화 추가
    path("new/", views.movie_new, name="movie_new"),
    # 영화 수정
    path("<int:pk>/edit/", views.movie_edit, name="movie_edit"),
    # 영화 삭제
    path("<int:pk>/delete/", views.movie_delete, name="movie_delete"),
    # 리뷰 추가
    path("<int:movie_pk>/review/new/", views.review_new, name="review_new"),
    # 리뷰 수정
    path("<int:movie_pk>/review/<int:pk>/edit/", views.review_edit, name="review_edit"),
    # 리뷰 삭제
    path(
        "<int:movie_pk>/review/<int:pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
    # 비디오 추가
    path("<int:movie_pk>/video/new/", views.video_new, name="video_new"),
    # 비디오 수정
    path("<int:movie_pk>/video/<int:pk>/edit/", views.video_edit, name="video_edit"),
    path(
        "<int:movie_pk>/video/<int:pk>/delete/", views.video_delete, name="video_delete"
    ),
]
