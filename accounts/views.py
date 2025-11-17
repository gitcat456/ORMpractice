from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from accounts.forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    