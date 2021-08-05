from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
]
