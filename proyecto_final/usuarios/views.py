from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Avatar
from .forms import UserRegisterForm, UserEditForm

from django.contrib.auth.models import User


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "usuarios/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "usuarios/base.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "usuarios/base.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                user = form.save(commit=False)
                user.set_password(password1)
                user.save()
                return render(request, "usuarios/pagina_principal.html", {"mensaje": username})
            else:
                form.add_error('password2', 'Las contraseñas no coinciden.')
    else:
        form = UserRegisterForm()
    return render(request, "usuarios/registro.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()
            return render(request, 'usuarios/pagina_principal.html')
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})

    return render(request, "usuarios/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


def main(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    avatar_url = avatar.imagen.url if avatar else None

    # context = {
    #     'avatar_url': avatar_url
    # }
    return render(request, 'usuarios/pagina_principal.html')


def index(request):
    return render(request, 'usuarios/pagina_principal.html')