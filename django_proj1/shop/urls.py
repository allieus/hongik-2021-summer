from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
]
