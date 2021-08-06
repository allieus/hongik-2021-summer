from django.urls import path

from journal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("new/", views.post_new, name="post_new"),
]
