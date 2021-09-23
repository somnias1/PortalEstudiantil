from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import EstudianteSerializer
from cerberus import Validator

class EstudianteApi(APIView):
    def post(self, request):
        validator = Validator({
            "cedula":{'required': True, "type": 'integer', 'min':1000000, "max": 9999999999}, 
            "first_name":{"required": True, "type": "string", 'maxlength': 128}, 
            "last_name":{"required": True, "type": "string", 'maxlength': 128}, 
            "residencia":{"required": True, "type": "string", 'maxlength': 255}, 
            "email":{"required": True, "type": "string"}
            })  
        if not validator.validate(request.data):
            return Response({'Errores':validator.errors}, status = status.HTTP_400_BAD_REQUEST)

        serializer = EstudianteSerializer()
        serializer.create(request.data)

        return Response({"Success": "Estudiante creado"}, status = status.HTTP_201_CREATED)

    def get(self, request):
        serializer = EstudianteSerializer()
        estudiantes = serializer.get_estudiantes()
        return Response(
            {
                "Información": estudiantes
            }, status = status.HTTP_200_OK)

    def delete(self, request):
        if not request.GET.get("id"):
            return Response({
                "Error": "Id inválido"
            }, status = status.HTTP_400_BAD_REQUEST)

        serializer = EstudianteSerializer()
        serializer.remove_estudiantes(request.GET["id"])
        return Response({"Exito": "Estudiante eliminado"}, status = status.HTTP_200_OK)

    def patch(self, request): 
        validator = Validator({
            "cedula":{'required': False, "type": 'integer', 'min':1000000, "max": 9999999999}, 
            "first_name":{"required": False, "type": "string", 'maxlength': 128}, 
            "last_name":{"required": False, "type": "string", 'maxlength': 128}, 
            "residencia":{"required": False, "type": "string", 'maxlength': 255}, 
            "email":{"required": False, "type": "string"}
            }) 

        if not validator.validate(request.data):
            return Response({'Errores': validator.errors}, 
            status=status.HTTP_400_BAD_REQUEST)

        if not request.GET.get('id'):
            return Response({'Error': 'Falta id'}, 
            status=status.HTTP_400_BAD_REQUEST)

        serializer = EstudianteSerializer()
        print(request.GET['id'])
        print(type(request.GET['id']))
        serializer.update_estudiantes(int(request.GET['id']), request.data)

        return Response(status=status.HTTP_202_ACCEPTED)
        

