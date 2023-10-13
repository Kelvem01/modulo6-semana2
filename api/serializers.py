from rest_framework import serializers

from eventos.models import Categoria, Evento

class CategoriaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        field = [
            'id',
            'nome',
            'slug',
            
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
