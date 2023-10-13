import json
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from eventos.models import Categoria , Evento

from api.serializers import CategoriaSerializers , EventoSerializer

"""
/api/categiria/ - GET : listando
/api/categiria/ - POST : criando
/api/categiria/ - PUT : consultando registro
/api/categiria/ - PATCH : atualizando 1 registro parcialmente
/api/categiria/ - DELETE : apagando 1 registro
"""


class CategoriaViewSet(ModelViewSet):
    
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.all()
    
   

class EventoViewSet(ModelViewSet):
    
    serializer_class = EventoSerializer
    
    def get_queryset(self):
        #return Evento.objects.filter(criado_por=self.request.user)
        
        return Evento.objects.all()
    
    def perform_create (self , serializer):
        
        if self.request.user.is_authenticated:
            serializer.save(criado_por =self.request.user)
        else:
            serializer.save()