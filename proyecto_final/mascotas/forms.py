from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Mascota

class NuevaMascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('titulo', 'especie', 'edad', 'descripcion', 'telefonoContacto', 'emailContacto', 'imagenMascota' )

    
class EditarMascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('titulo', 'especie', 'edad', 'descripcion', 'telefonoContacto', 'emailContacto', 'imagenMascota')
    