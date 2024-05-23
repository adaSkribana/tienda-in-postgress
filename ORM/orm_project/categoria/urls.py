from django.urls import path
from .views import CategoriaListView, CategoriaDetailView, categoria_crear, categoria_editar

app_name = 'categoria'

urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria_lista'),
    path('<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detalle'),
    path('crear/', categoria_crear, name='categoria_crear'),
    path('editar/<int:pk>/', categoria_editar, name='categoria_editar'),
]
