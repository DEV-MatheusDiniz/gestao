from datetime import datetime

from rest_framework import serializers

from api.usuario.models.usuario import UsuarioModel


class UsuarioSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y %H:%M:%S")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y %H:%M:%S")

        usuario = {
            "id": instance.id,
            "no_nome": instance.no_nome,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

        return usuario
    
    class Meta:
        model = UsuarioModel
        fields = "__all__"
