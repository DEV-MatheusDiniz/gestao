from django.db import models

from api.tarefa.models.tarefa import TarefaModel


class AtividadeModel(models.Model):
    dt_inicio = models.DateTimeField()
    dt_fim = models.DateTimeField()
    ds_descricao = models.TextField()
    fk_tarefa = models.ForeignKey(TarefaModel, on_delete=models.CASCADE)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.ds_descricao

    class Meta:
        app_label = "atividade"
        db_table = "atividades"
