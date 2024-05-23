from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CategoriaForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_lista.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria/categoria_detalle.html'
    context_object_name = 'categoria'

@login_required
def categoria_crear(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:categoria_lista')  # Corregido el nombre de la URL
    else:
        form = CategoriaForm()
    return render(request, 'categoria/categoria_crear.html', {'form': form})

@login_required
def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:categoria_lista')  # Corregido el nombre de la URL
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/categoria_editar.html', {'form': form})
