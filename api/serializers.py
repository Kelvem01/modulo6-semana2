from rest_framework import serializers

from eventos.models import Categoria, Evento, InscricaoEvento
from rest_framework.serializers import PrimaryKeyRelatedField


class CategoriaEventoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Evento
        fields =[
            'id',
            'nome',
            'data',
            'descricao',
            'criado_em',
            'criado_por',
        ]
        
class CategoriaInscricaoEventoSerializer(serializers.ModelSerializer):
    
   class Meta: 
        model = InscricaoEvento
        fields = [
            'id',
            'email',
            'evento',
            'confirmado',
            'criado_em',
            'modificado_em',
        ]

class CategoriaSerializers(serializers.ModelSerializer):
    
    eventos = CategoriaEventoSerializer(many=True)
    inscricoes = serializers.SerializerMethodField(method_name='listar_inscricoes')
    
    def listar_inscricoes(self,obj):
        eventos = obj.eventos.all()
        inscricoes = InscricaoEvento.objects.filter(evento__in=eventos.values('pk'))
        serializer = CategoriaInscricaoEventoSerializer(instance=inscricoes,many=True)
        return serializer.data
    
    
    class Meta:
        model = Categoria
        field = [
            'id',
            'nome',
            'slug',
            'eventos',
            'inscricoes',
        ]    
    
class EventoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Evento
        fields=[
            'id',
            'nome',
            'categoria',
            'data',
            'descricao',
            'criado_em',
            'criado_por',
            
        ]
        
class PrimaryKeyEventoField(PrimaryKeyRelatedField):
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        serializer = EventoSerializer(instance=value)
        return serializer.data

class InscricaoEventoSerializer(serializers.ModelSerializer):
    
    evento = PrimaryKeyEventoField(queryset=Evento.objects.all())
    
    class Meta :
        model = InscricaoEvento
        fields = [
            'id',
            'email',
            'evento',
            'confirmado',
            'criado_em',
            'modificado_em',
             
        ]
        