from datetime import datetime

from rest_framework import serializers

from api.tarefa.models.tarefa import TarefaModel

from api.usuario.serializers.usuario import UsuarioSerializer


class TarefaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y %H:%M:%S")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y %H:%M:%S")

        fk_responsavel = UsuarioSerializer(instance.fk_responsavel).data

        tarefa = {
            "id": instance.id,
            "ds_descricao": instance.ds_descricao,
            "fk_responsavel": fk_responsavel,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

        return tarefa
    
    class Meta:
        model = TarefaModel
        fields = "__all__"
