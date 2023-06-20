from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mascotas.models import Mascota
from mascotas.forms import NuevaMascotaForm, EditarMascotaForm

# REGISTRO DE MASCOTA
class CrearMascota(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = NuevaMascotaForm
    success_url = reverse_lazy('mascotas')
    template_name = 'mascotas/registroMascota.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearMascota, self).form_valid(form)



# CRUD PERROS
class PerroList(LoginRequiredMixin, ListView):
    context_object_name = 'perros'
    queryset = Mascota.objects.filter(especie__startswith= 'perro')
    template_name = 'mascotas/listaPerros.html'
    
class PerroDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'perro'
    template_name = 'mascotas/detallePerros.html'
    
class PerroUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = EditarMascotaForm
    success_url = reverse_lazy('perros')
    context_object_name = 'perro'
    template_name = 'mascotas/editarPerros.html'
    
class PerroDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('perros')
    context_object_name = 'perro'
    template_name = 'mascotas/eliminadoPerros.html'
    
    
    
# CRUD GATOS
class GatoList(LoginRequiredMixin, ListView):
    context_object_name = 'gatos'
    queryset = Mascota.objects.filter(especie__startswith= 'gato')
    template_name = 'mascotas/listaGatos.html'
    
class GatoDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'gato'
    template_name = 'mascotas/detalleGatos.html'
    
class GatoUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = EditarMascotaForm
    success_url = reverse_lazy('gatos')
    context_object_name = 'gato'
    template_name = 'mascotas/editarGatos.html'
    
class GatoDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('gatos')
    context_object_name = 'gato'
    template_name = 'mascotas/eliminadoGatos.html'



# CRUD OTROS
class OtroList(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Mascota.objects.filter(especie__startswith= 'otro')
    template_name = 'mascotas/listaOtros.html'
    
class OtroDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'otro'
    template_name = 'mascotas/detalleOtro.html'
    
class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = EditarMascotaForm
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'mascotas/editarOtros.html'
    
class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'mascotas/eliminadoOtros.html'

