from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



from django.views.generic import FormView
from .forms import RegisterForm, LoginForm

# User = get_user_model()

class RegisterFormView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        print(user)
        return super().form_valid(form)



class LoginFormView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)