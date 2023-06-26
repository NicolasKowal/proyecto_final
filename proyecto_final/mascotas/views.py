from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from mascotas.models import Mascota


# CRUD MASCOTA
class CrearMascota(LoginRequiredMixin, CreateView):
    model = Mascota
    template_name = 'mascotas/registroMascota.html'
    fields = ['titulo', 'especie', 'edad', 'descripcion', 'telefonoContacto', 'emailContacto', 'imagenMascota']
    success_url = reverse_lazy('lista mascotas')
    login_url = reverse_lazy('Login')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MascotasList(ListView):
    model = Mascota
    template_name = 'mascotas/listaMascotas.html'
    
        
class MascotaDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'mascotas/detalleMascota.html'
    login_url = reverse_lazy('Login')
    
class MascotaUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    fields = ['titulo', 'especie', 'edad', 'descripcion', 'telefonoContacto', 'emailContacto', 'imagenMascota']
    context_object_name = 'mascota'
    template_name = 'mascotas/editarMascota.html'
    success_url = reverse_lazy('lista mascotas')

    
class MascotaDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'mascotas/eliminarMascota.html'
    success_url = reverse_lazy('lista mascotas')


# LISTA PERROS
class PerroList(ListView):
    queryset = Mascota.objects.filter(especie__startswith= 'perro')
    context_object_name = 'perros'
    template_name = 'mascotas/listaPerros.html'
    
    
# LISTA GATOS
class GatoList(ListView):
    queryset = Mascota.objects.filter(especie__startswith= 'gato')
    context_object_name = 'gatos'
    template_name = 'mascotas/listaGatos.html'
    

# LISTA OTROS
class OtroList(ListView):
    queryset = Mascota.objects.filter(especie__startswith= 'otro')
    context_object_name = 'otros'
    template_name = 'mascotas/listaOtros.html'
    

