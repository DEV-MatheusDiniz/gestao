from datetime import datetime

from rest_framework import serializers

from api.atividade.models.atividade import AtividadeModel

from api.tarefa.serializers.tarefa import TarefaSerializer


class AtividadeSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_inicio = datetime.strftime(instance.dt_inicio, "%d/%m/%Y %H:%M:%S")
        dt_fim = datetime.strftime(instance.dt_fim, "%d/%m/%Y %H:%M:%S")
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y %H:%M:%S")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y %H:%M:%S")
        nu_tempo_trabalhado = instance.dt_fim - instance.dt_inicio

        fk_tarefa = TarefaSerializer(instance.fk_tarefa).data

        atividade = {
            "id": instance.id,
            "dt_inicio": dt_inicio,
            "dt_fim": dt_fim,
            "nu_tempo_trabalhado": str(nu_tempo_trabalhado),
            "ds_descricao": instance.ds_descricao,
            "fk_tarefa": fk_tarefa,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

        return atividade
    
    class Meta:
        model = AtividadeModel
        fields = "__all__"
