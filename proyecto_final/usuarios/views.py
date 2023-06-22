from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Avatar
from .forms import UserRegisterForm, EditarPerfil, EditPassword

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


def main(request):
    return render(request, 'usuarios/pagina_principal.html')


def index(request):
    return render(request, 'usuarios/index.html')


@login_required
def editarPerfil(request):
    if request.method == 'POST':
        form = EditarPerfil(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = EditarPerfil(instance=request.user)

    return render(request, 'usuarios/editarperfil.html', {'form': form})


@login_required
def editarPass(request):
    if request.method == 'POST':
        form = EditPassword(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = EditPassword(instance=request.user)

    return render(request, 'usuarios/editarpassw.html', {'form': form})






from django.shortcuts import render, redirect
from .forms import AvatarForm
from django.contrib.auth.decorators import login_required

@login_required
def cambiarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
        return redirect('main') 

    else:
        form = AvatarForm(instance=request.user)

    return render(request, 'usuarios/cambiar_avatar.html', {'form': form})