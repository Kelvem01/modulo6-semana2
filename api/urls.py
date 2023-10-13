from django.urls import path

from rest_framework.routers import DefaultRouter

from api.views import CategoriaViewSet, EventoViewSet

app_name = 'api'

router = DefaultRouter()
router.register('categorias',CategoriaViewSet,basename='categorias')
router.register('eventos',EventoViewSet,basename='eventos')


urlpatternes = []


urlpatternes = urlpatternes + router.urls 