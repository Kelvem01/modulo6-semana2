from django.urls import path

from rest_framework.routers import DefaultRouter

from api.views import CategoriaViewSet, EventoViewSet , InscricaoEventoViewSet

app_name = 'api'

router = DefaultRouter()
router.register('categorias',CategoriaViewSet,basename='categorias')
router.register('eventos',EventoViewSet,basename='eventos')
router.register('inscricoes-eventos',InscricaoEventoViewSet,basename='inscricoes-eventos')

urlpatterns = []


urlpatterns = urlpatterns + router.urls 