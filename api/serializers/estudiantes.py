from rest_framework import serializers
from ..models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estudiante
        fields = ["cedula", "first_name", "last_name", "email", "is_active"]

    def create(self, validate_data):
        estudiante = Estudiante.objects.create(**validate_data).id
        return estudiante

    def get_estudiantes(self):
        return EstudianteSerializer(Estudiante.objects.all(), many=True).data

    def remove_estudiantes(self, id):
        estudiante = Estudiante.objects.filter(id=id).update(is_active=False)
        return estudiante


    def update_estudiantes(self, id, validate_data):
        estudiante = Estudiante.objects.filter(id=id).update(**validate_data)
        return estudiante
