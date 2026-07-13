from django.urls import path

from .views import RegisterFormView, LoginFormView

urlpatterns=[

path("register/", RegisterFormView.as_view(template_name="registration/register.html"), name="register"),
path("login/", LoginFormView.as_view(template_name="registration/login.html"), name="login"),


]

