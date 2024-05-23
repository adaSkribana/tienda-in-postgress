from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Producto
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_lista.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detalle.html'
    context_object_name = 'producto'

@login_required
def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:producto_lista')  # Corregido el nombre de la URL
    else:
        form = ProductoForm()
    return render(request, 'productos/producto_crear.html', {'form': form})

@login_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:producto_lista')  # Corregido el nombre de la URL
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_editar.html', {'form': form})
