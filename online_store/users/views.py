from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm, LoginForm


# User = get_user_model()

class RegisterFormView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class LoginFormView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)