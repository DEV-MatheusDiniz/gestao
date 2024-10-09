from rest_framework import viewsets

from api.tarefa.models.tarefa import TarefaModel
from api.tarefa.serializers.tarefa import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = TarefaModel.objects.all()
    serializer_class = TarefaSerializer
