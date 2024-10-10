from datetime import datetime

from rest_framework import serializers

from api.atividade.models.atividade import AtividadeModel

from api.tarefa.serializers.tarefa import TarefaSerializer


class AtividadeSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_inicio = datetime.strftime(instance.dt_inicio, "%d/%m/%Y - %H:%M")
        dt_fim = datetime.strftime(instance.dt_fim, "%d/%m/%Y - %H:%M")
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        # Calcular a diferença entre as datas de fim e inicio
        delta = instance.dt_fim - instance.dt_inicio
        total_segundos = delta.total_seconds()
        horas_totais = total_segundos // 3600
        minutos_totais = (total_segundos % 3600) // 60
        nu_tempo_trabalhado = f"{int(horas_totais):02}:{int(minutos_totais):02}"

        fk_tarefa = TarefaSerializer(instance.fk_tarefa).data

        atividade = {
            "id": instance.id,
            "dt_inicio": dt_inicio,
            "dt_fim": dt_fim,
            "nu_tempo_trabalhado": nu_tempo_trabalhado,
            "ds_descricao": instance.ds_descricao,
            "fk_tarefa": fk_tarefa,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

        return atividade
    
    class Meta:
        model = AtividadeModel
        fields = "__all__"
