from rest_framework import viewsets

from api.atividade.models.atividade import AtividadeModel
from api.atividade.serializers.atividade import AtividadeSerializer


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = AtividadeModel.objects.all()
    serializer_class = AtividadeSerializer
