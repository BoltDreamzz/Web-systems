from django.urls import path

from . import views

app_name = "authusers"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("splash/", views.splash, name="splash"),
]












