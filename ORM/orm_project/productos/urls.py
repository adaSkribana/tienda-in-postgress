
from django.urls import path
from .views import ProductoListView, ProductoDetailView, producto_crear, producto_editar

app_name = 'productos'

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_lista'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),
    path('crear/', producto_crear, name='producto_crear'),
    path('editar/<int:pk>/', producto_editar, name='producto_editar'),
]
