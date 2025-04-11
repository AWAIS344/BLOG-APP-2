from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",LoginView.as_view(),name="auth-login"),
    path("logout/",LogoutView.as_view(),name="auht-logout"),

]
