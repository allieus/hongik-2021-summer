from django.urls import path

from travel import views

urlpatterns = [
    path("", views.index, name="index"),
]
