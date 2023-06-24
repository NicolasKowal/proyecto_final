from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mascotas.models import Mascota
from mascotas.forms import EditarMascotaForm #NuevaMascotaForm

# CRUD MASCOTA
class CrearMascota(LoginRequiredMixin, CreateView):
    model = Mascota
    template_name = 'mascotas/registroMascota.html'
    fields = ['titulo', 'especie', 'edad', 'descripcion', 'telefonoContacto', 'emailContacto']
    success_url = reverse_lazy('lista mascotas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.imagenMascota = self.request.FILES.get('imagenMascota')
        return super().form_valid(form)


# CRUD MASCOTA
class MascotasList(ListView):
    model = Mascota
    template_name = 'mascotas/listaMascotas.html'
    

class MascotaDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'mascotas/detalleMascota.html'
    
class MascotaUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = EditarMascotaForm
    success_url = reverse_lazy('lista mascotas')
    context_object_name = 'lista mascotas'
    
class MascotaDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('lista mascotas')
    context_object_name = 'lista mascotas'
    template_name = 'mascotas/listaMascotas.html'


# LISTA PERROS
class PerroList(LoginRequiredMixin, ListView):
    context_object_name = 'perros'
    queryset = Mascota.objects.filter(especie__startswith= 'perro')
    template_name = 'mascotas/listaPerros.html'
    
    
# LISTA GATOS
class GatoList(LoginRequiredMixin, ListView):
    context_object_name = 'gatos'
    queryset = Mascota.objects.filter(especie__startswith= 'gato')
    template_name = 'mascotas/listaGatos.html'
    

# LISTA OTROS
class OtroList(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Mascota.objects.filter(especie__startswith= 'otro')
    template_name = 'mascotas/listaOtros.html'
    

