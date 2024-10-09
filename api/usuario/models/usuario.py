from django.db import models


class UsuarioModel(models.Model):
    no_nome = models.CharField(max_length=50)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.no_nome

    class Meta:
        app_label = "usuario"
        db_table = "usuarios"
