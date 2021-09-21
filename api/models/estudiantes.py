from django.db import models
from datetime import timedelta, date

from django.contrib.auth.models import AbstractUser

class Estudiante(AbstractUser):
    cedula = models.IntegerField('Cédula del estudiante', unique=True)
    USERNAME_FIELD = 'cedula'
    REQUIRED_FIELDS = ['username']
    first_name = models.CharField('Nombre', max_length=128, blank=True, null= True)
    last_name = models.CharField('Apellido', max_length=128, blank=True, null= True)
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", 
        help_text= "YYYY-MM--DD", blank=True, null= True)
    residencia = models.CharField('Dirección de residencia', max_length=255, blank=True, null= True)
    email = models.EmailField(blank = True, null = True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.cedula} - {self.first_name} - {self.last_name}"
