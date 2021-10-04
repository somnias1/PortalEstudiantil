from django.urls import include, path
from .views import UsuarioRegistroApi


urlpatterns = [path("usuarios/registro", UsuarioRegistroApi.as_view())]
