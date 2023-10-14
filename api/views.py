


from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly ,SAFE_METHODS
from rest_framework.response import Response
from django_filters.filterset import FilterSet

from eventos.models import Categoria , Evento

from api.serializers import CategoriaSerializers , EventoSerializer


class CategoriaViewSet(ModelViewSet):
    
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['nome','slug']
    
    
    @action(detail=True, methods=['GET'])
    def eventos(self,request,pk):
        categoria = self.get_object()
        #eventos = Evento.objects.filter(categoria=categoria)
        eventos = categoria.eventos.all()
        serializer = EventoSerializer(instance=eventos, many = True)
        return Response (data=serializer.data)
        
class EventoFilterSet(FilterSet):
    class Meta :
        model = Evento
        fields ={
            'categoria' : ['exact'],
            'nome' : ['icontains'],
            'descricao' : ['icontains'],
        }

class EventoViewSet(ModelViewSet):
    
    serializer_class = EventoSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    filterset_class = EventoFilterSet
    
    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            return Evento.objects.all()
        return Evento.objects.filter(criado_por=self.request.user)
        
    
    def perform_create (self , serializer):
        serializer.save(criado_por =self.request.user)
