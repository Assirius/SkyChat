from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]