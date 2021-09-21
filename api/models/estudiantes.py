from django.db import models
from datetime import timedelta, date

from django.contrib.auth.models import AbstractUser

class Estudiante(AbstractUser):
    cedula = models.IntegerField('Cédula del estudiante', unique=True)
    USERNAME_FIELD = 'cedula'
    username = None
    nombre_1 = models.CharField('Primer nombre', max_length=128, blank=True, null= True)
    nombre_2 = models.CharField('Primer nombre', max_length=128, blank=True, null= True)
    Apellido_1 = models.CharField('Primer nombre', max_length=128, blank=True, null= True)
    apellido_2 = models.CharField('Primer nombre', max_length=128, blank=True, null= True)
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", 
        help_text= "YYYY-MM--DD", blank=True, null= True)
    residencia = models.CharField('Dirección de residencia', max_length=255, blank=True, null= True)


    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.cedula} - {self.nombre_1} - {self.apellido_1}"
