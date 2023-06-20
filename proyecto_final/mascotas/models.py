from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mascota(models.Model):
    especieSeleccion = (
    ('perro','Perro'),
    ('gato', 'Gato'),
    ('otro','Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    especie = models.CharField(max_length=15, choices=especieSeleccion, default='otro')
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenMascota = models.ImageField(null=True, blank=True, upload_to="media/imagenes/")
    
    def __str__(self):
        return f" {self.titulo} \n- Especie: {self.especie} \n- Publicado: {self.fechaPublicacion}\n- Usuario: {self.usuario}"
