from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(
        template_name='usuarios/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('', views.index, name='index'),
    path('Pagina_principal', views.main, name='main'),
    path('Editar_perfil', views.editarPerfil, name='editarPerfil'),
    path('Editar_contrasena', views.editarContraseña, name='editarContrasena'),
    path('AcercaDe', views.aboutUs, name='AboutUs'),
    path('cambiar-avatar', views.cambiarAvatar, name='cambiar_avatar'),
    path('Not-found', views.error, name='error')
]
