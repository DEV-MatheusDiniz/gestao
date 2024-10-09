from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.usuario.views.usuario import UsuariosViewSet


router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
