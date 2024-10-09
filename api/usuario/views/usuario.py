from rest_framework import viewsets

from api.usuario.models.usuario import UsuarioModel
from api.usuario.serializers.usuario import UsuarioSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
