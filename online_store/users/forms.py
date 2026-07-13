from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()



class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email


class LoginForm(AuthenticationForm):
    pass
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Парола'}))
