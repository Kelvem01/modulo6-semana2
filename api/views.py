import json
from django.http import HttpResponse
from eventos.models import Categoria

def categorias (request):
    consulta = Categoria.objects.all()
    dados = []
    for categoria in consulta :
        dado ={
            'id': categoria.id,
            'nome': categoria.nome,
            'slug': categoria.slug,
            
        }
        dados.append(dado)
    return HttpResponse(json.dumps(dados))
