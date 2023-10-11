from django.urls import path
from api.views import categorias , adicionar_categoria, eventos

app_name = 'api'

urlpatternes = [
    path('categorias/',categorias,name ='categorias')
    path('adicionar_categoria/',adicionar_categoria, name ='adicionar_categoria')
    path('eventos/',eventos,name ='eventos')
]