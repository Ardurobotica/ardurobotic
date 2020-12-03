from django.db import models

# Create your models here.
class Recomendacion(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    razon = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

