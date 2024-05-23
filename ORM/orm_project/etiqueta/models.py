# Create your models here.

from django.db import models
from productos.models import Producto

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    
    def __str__(self):
        return self.nombre

