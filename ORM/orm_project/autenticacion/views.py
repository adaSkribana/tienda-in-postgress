# autenticacion/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'autenticacion/login.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('autenticacion:login')
    template_name = 'autenticacion/signup.html'
