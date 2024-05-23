from django.db import models
from django.db import models
from django.contrib.auth.models import User
from categoria.models import Categoria 
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
