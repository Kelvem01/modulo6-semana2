


from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import  IsAuthenticatedOrReadOnly ,SAFE_METHODS , AllowAny , IsAdminUser
from rest_framework.response import Response
from django_filters.filterset import FilterSet

from eventos.models import Categoria , Evento , InscricaoEvento

from api.serializers import CategoriaSerializers , EventoSerializer , InscricaoEventoSerializer


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
        
class InscricaoEventoFilterSet(ModelViewSet):
    class Meta:
        model = InscricaoEvento
        fields = {
            'evento':['exact'],
            'nome' : ['icontains'],
            'email' : ['icontains'],
            'criado_em' : ['gte','lte'],
        }


class InscricaoEventoViewSet(ModelViewSet):
    
    serializer_class = InscricaoEventoSerializer
    queryset = InscricaoEvento.objects.all()
    filterset_clas= ['evento']
    
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]