from django.db import models

from api.usuario.models.usuario import UsuarioModel


class TarefaModel(models.Model):
    ds_descricao = models.TextField()
    responsavel = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = "tarefa"
        db_table = "tarefas"
