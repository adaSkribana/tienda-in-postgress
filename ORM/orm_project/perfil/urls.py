# perfil/urls.py
from django.urls import path
from . import views
from .views import PerfilDetailView, PerfilUpdateView


app_name = 'perfil'

urlpatterns = [
    path('crear/', views.perfil_crear, name='perfil_crear'),
    path('detalle/', PerfilDetailView.as_view(), name='perfil_detalle'),
    path('editar/', PerfilUpdateView.as_view(), name='perfil_editar'),
]
