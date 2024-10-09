from datetime import datetime

from rest_framework import serializers

from api.usuario.models.usuario import UsuarioModel


class UsuarioSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y %H:%M:%S")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y %H:%M:%S")

        usuario = {}
        usuario["id"] = instance.id
        usuario["no_nome"] = instance.no_nome
        usuario["dt_cadastro"] = dt_cadastro
        usuario["dt_alteracao"] = dt_alteracao

        return usuario
    
    class Meta:
        model = UsuarioModel
        fields = "__all__"
