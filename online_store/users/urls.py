from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import FormView
from .views import RegisterFormView,LoginFormView


urlpatterns=[

path("register/", RegisterFormView.as_view(template_name="users/register.html")),
path("login/", LoginFormView.as_view(template_name="users/login.html"))

]

