from django.views.generic import ListView, DetailView
from .models import Etiqueta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EtiquetaForm

class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'etiqueta/etiqueta_lista.html'
    context_object_name = 'etiquetas'

class EtiquetaDetailView(DetailView):
    model = Etiqueta
    template_name = 'etiqueta/etiqueta_detalle.html'
    context_object_name = 'etiqueta'

@login_required
def etiqueta_crear(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etiqueta:etiqueta_lista')
    else:
        form = EtiquetaForm()
    return render(request, 'etiqueta/etiqueta_crear.html', {'form': form})

@login_required
def etiqueta_editar(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('etiqueta:etiqueta_lista')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiqueta/etiqueta_editar.html', {'form': form})
