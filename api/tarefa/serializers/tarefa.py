from datetime import datetime

from rest_framework import serializers

from api.tarefa.models.tarefa import TarefaModel


class TarefaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y %H:%M:%S")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y %H:%M:%S")

        tarefa = {}
        tarefa["id"] = instance.id
        tarefa["ds_descricao"] = instance.ds_descricao
        tarefa["responsavel"] = instance.responsavel.no_nome
        tarefa["dt_cadastro"] = dt_cadastro
        tarefa["dt_alteracao"] = dt_alteracao

        return tarefa
    
    class Meta:
        model = TarefaModel
        fields = "__all__"
