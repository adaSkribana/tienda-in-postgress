# perfil/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Perfil
from .forms import PerfilForm

@method_decorator(login_required, name='dispatch')
class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'perfil/perfil_detalle.html'
    context_object_name = 'perfil'

    def get_object(self):
        return get_object_or_404(Perfil, usuario=self.request.user)

@method_decorator(login_required, name='dispatch')
class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'perfil/perfil_editar.html'
    success_url = reverse_lazy('perfil:perfil_detalle')

    def get_object(self):
        return get_object_or_404(Perfil, usuario=self.request.user)


@login_required
def perfil_editar(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil:perfil_detalle')  # Corregido el nombre de la URL
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil/perfil_editar.html', {'form': form})

@login_required
def perfil_crear(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil:perfil_detalle')  # Corregido el nombre de la URL
    else:
        form = PerfilForm()
    return render(request, 'perfil/perfil_crear.html', {'form': form})
