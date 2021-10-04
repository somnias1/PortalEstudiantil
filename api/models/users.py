from django.db import models
from datetime import timedelta, date

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    users = [
        ("est", "Estudiante"),
        ("adm", "Administrativo"),
        ("prof", "Profesor")
    ]
    cedula = models.CharField("Cédula del usuario", unique=True, max_length=10)
    nombre = models.CharField("Nombre", max_length=128, blank=True, null=True)
    apellido = models.CharField("Apellido", max_length=128, blank=True, null=True)
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", help_text="YYYY-MM--DD", blank=True, null=True
    )
    residencia = models.CharField(
        "Dirección de residencia", max_length=255, blank=True, null=True
    )
    email = models.EmailField(blank=True, null=True)

    tipo_usuario = models.CharField(choices=users, null=False, max_length=32)

    USERNAME_FIELD = "cedula"
    FIRST_NAME_FIELD = "nombre"
    LAST_NAME_FIELD = "apellido"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.cedula} - {self.nombre} - {self.apellido}"
