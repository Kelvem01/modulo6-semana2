from django.shortcuts import render 
from base.forms import InscreverForm
from base.models import Contato

# Create your views here.
def inicio(request):
    dados = []
    dados . append(
        {
            'titulo': 'Titulo legal 1',
            'categoria': 'Categoria 1',
            'data': '30/08/2023',
        }
        
    )
    dados.append(
        {
            'titulo' : 'Titulo legal 2',
            'categoria' : 'Categoria 2',
            'data ' : ' 29/08/2023',
        }
        
    )
    contexto = {
        'dados ' : dados 
    }
    
    resposta = render (request , 'inicio.html', contexto)
    return resposta

def inscrever(request):
    sucesso = False
    form = InscreverForm (request.POST or None)

    if form.is_valid ():
        form.save()
        sucesso = True
    else:
        form = InscreverForm ()
        
    contexto = {
        'sucesso':sucesso,
        'form' : form,
    }
    return render(request , "inscrever.html" , contexto)