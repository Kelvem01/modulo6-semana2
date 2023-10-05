from django.urls import path
from api.views import categorias

app_name = 'api'

urlpatternes = [
    path('categorias/',categorias,name ='categorias')
                
]