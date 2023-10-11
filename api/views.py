import json
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from eventos.models import Categoria , Evento

@api_view()
def categorias (request):
    consulta = Categoria.objects.all()
    dados = []
    for categoria in consulta :
        dado ={
            'id': categoria.id,
            'nome': categoria.nome,
            'descricao': categoria.descricao,
            
        }
        dados.append(dado)
    return Response(dados)

@api_view(http_method_names=['POST'])
def adicionar_categoria(request):
    nome = request.data ['nome']
    descricao = request.data ['descricao']
    categoria = Categoria.objects.create(nome = nome , descricao = descricao)
    dado ={
        'id':categoria.id,
        'nome':categoria.nome,
        'descricao':categoria.descricao,
    }
    return Response(dado)

@api_view()
def eventos (request):
    consulta = Evento.objects.all()
    dados = []
    for evento in consulta:
        dado = {
            'nome': evento.nome,
            'categoria':{
                'id': evento.categoria.id,
                'nome': evento.categoria.nome,
                'descricao': evento.categoria.descricao,
            },
            'data': evento.data,
            'descricao': evento.descricao,
            'criado_em': evento.categoria,
        }
        dados.append(dado)
    return Response(dados) 
    
    
# def categorias (request):
#     consulta = Categoria.objects.all()
#     dados = []
#     for categoria in consulta :
#         dado ={
#             'id': categoria.id,
#             'nome': categoria.nome,
#             'descricao': categoria.descricao,
            
#         }
#         dados.append(dado)
#     return HttpResponse(json.dumps(dados))