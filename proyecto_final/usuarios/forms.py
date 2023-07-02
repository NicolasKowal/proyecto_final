from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password
from .models import Avatar


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class EditarPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'E-Mail'
        }

class EditarContraseña(UserChangeForm):
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user



class avatarForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Avatar
        fields = ['avatar']
