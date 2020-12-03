from django.db import models

# Create your models here.

class Mercancia (models.Model):
    fotografia = models.ImageField(upload_to='mercancias')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return str(self.fotografia)

