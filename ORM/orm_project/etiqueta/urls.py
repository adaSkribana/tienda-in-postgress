from django.urls import path
from .views import EtiquetaListView, EtiquetaDetailView, etiqueta_crear, etiqueta_editar

app_name = 'etiqueta'

urlpatterns = [
    path('', EtiquetaListView.as_view(), name='etiqueta_lista'),
    path('<int:pk>/', EtiquetaDetailView.as_view(), name='etiqueta_detalle'),
    path('crear/', etiqueta_crear, name='etiqueta_crear'),
    path('editar/<int:pk>/', etiqueta_editar, name='etiqueta_editar'),
]
