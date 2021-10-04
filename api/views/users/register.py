from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers import UsuarioSerializer
from cerberus import Validator


class UsuarioRegistroApi(APIView):
    def post(self, request):
        validator = Validator(
            {
                "cedula": {
                    "required": True,
                    "type": "string",
                    'regex':'[1-9][0-9]{6,10}'
                },
                "nombre": {"required": True, "type": "string", "maxlength": 128},
                "apellido": {"required": True, "type": "string", "maxlength": 128},
                "residencia": {"required": True, "type": "string", "maxlength": 255},
                "email": {"required": True, "type": "string"},
                "tipo_usuario": {"required": True, "type": "string"}
            }
        )
        if not validator.validate(request.data):
            return Response(
                {"Errores": validator.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UsuarioSerializer()
        serializer.create(request.data)

        return Response(
            {"Success": "Usuario creado"}, status=status.HTTP_201_CREATED
        )

