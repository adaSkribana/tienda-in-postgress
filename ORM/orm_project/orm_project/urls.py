# orm_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('categoria/', include('categoria.urls')),
    path('productos/', include('productos.urls')),
    path('etiqueta/', include('etiqueta.urls')),
    path('perfil/', include('perfil.urls')),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),  # URL para la página de inicio
    path('', RedirectView.as_view(url='autenticacion/login/', permanent=False)),  # Redirigir a la página de login en la raíz
]
