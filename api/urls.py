from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.usuario.views.usuario import UsuariosViewSet
from api.tarefa.views.tarefa import TarefaViewSet
from api.atividade.views.atividade import AtividadeViewSet


router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet)
router.register('tarefas', TarefaViewSet)
router.register('atividades', AtividadeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
