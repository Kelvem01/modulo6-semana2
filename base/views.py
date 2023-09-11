from django.shortcuts import render 
from base.forms import InscreverForm

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
    contexto = {'sucesso':False}
    form = InscreverForm (request.POST or None)

    if form.is_valid ():
        print(form.cleaned_data ['nome'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['observacao'])
        contexto['sucesso'] = True
    else:
        form = InscreverForm ()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request , "inscrever.html" , contexto)