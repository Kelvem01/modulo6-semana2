from django.urls import path
from eventos.views import eventos_detalhes

app_name = 'eventos'

urlpatterns = [
    path ('detalhes/<int:id>/',eventos_detalhes,name='eventos_detalhes'),
    
]