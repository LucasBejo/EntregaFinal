from re import M
from django.db import models

# Create your models here.
class Datos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    def __str__(self):
      return f"Nombre: {self.nombre}  --  Apellido: {self.apellido}  --  Edad: { self.edad}  "