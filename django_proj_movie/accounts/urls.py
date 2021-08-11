from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/",
         LoginView.as_view(template_name="accounts/login_form.html"),
         name="login"),
    path("logout/",
         # next_page 인자는 LogoutView 내부적으로 URL Reverse가 수행됩니다.
         LogoutView.as_view(next_page="login"),
         name="logout"),
    path("profile/", views.profile, name="profile"),
]
