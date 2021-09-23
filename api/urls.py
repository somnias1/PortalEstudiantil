from django.urls import include, path
from .views import EstudianteApi


urlpatterns = [path("estudiantes", EstudianteApi.as_view())]
