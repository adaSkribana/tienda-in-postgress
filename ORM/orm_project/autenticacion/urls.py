# autenticacion/urls.py
from django.urls import path
from .views import CustomLoginView, SignUpView
from django.contrib.auth.views import LogoutView

app_name = 'autenticacion'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='autenticacion:login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
