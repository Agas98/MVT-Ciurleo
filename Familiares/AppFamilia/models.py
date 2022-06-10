from django.db import models

# Create your models here.
class parientesPorPadre(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()

class parientesPorMadre(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()
    
