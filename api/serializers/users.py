from rest_framework import serializers
from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["cedula", "nombre", "apellido", "email", "tipo_usuario"]

    def create(self, validate_data):
        usuario = Usuario.objects.create(**validate_data).id
        return usuario

    def get_usuarios(self):
        return UsuarioSerializer(User.objects.all(), many=True).data

    def remove_usuarios(self, id):
        usuario = Usuario.objects.filter(id=id).update(is_active=False)
        return usuario

    def update_usuarios(self, id, validate_data):
        usuario = Usuario.objects.filter(id=id).update(**validate_data)
        return usuario
