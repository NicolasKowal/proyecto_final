from django.contrib import admin
from django.urls import path, include
from mascotas import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('listado-mascotas/', views.MascotasList.as_view(), name="lista mascotas"),
    path('crear-mascota/', views.CrearMascota.as_view(), name="crear mascota"),
    path('detalleMascota/<pk>/', views.MascotaDetail.as_view(), name="detalle mascota"),
    path('editarMascota/<pk>/', views.MascotaUpdate.as_view(), name="editar mascota"),
    path('eliminarMascota/<pk>/', views.MascotaDelete.as_view(), name="eliminar mascota"),
    path('lista-perros/', views.PerroList.as_view(), name="perros"),
    path('lista-gatos/', views.GatoList.as_view(), name="gatos"),
    path('lista-otros/', views.OtroList.as_view(), name="otros"),
    # path('editarPerro/<pk>/', views.PerroUpdate.as_view(), name="editar perro"),
    # path('editarGato/<pk>/', views.GatoUpdate.as_view(), name="editar gato"),
    # path('editarOtro/<pk>/', views.OtroUpdate.as_view(), name="editar otro"),
    # path('eliminarPerro/<pk>/', views.PerroDelete.as_view(), name="eliminar perro"),
    # path('eliminarGato/<pk>/', views.GatoDelete.as_view(), name="eliminar gato"),
    # path('eliminarOtro/<pk>/', views.OtroDelete.as_view(), name="eliminar otro"),
]
