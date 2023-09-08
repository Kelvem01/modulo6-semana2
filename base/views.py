from django.shortcuts import render 

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
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        contexto['sucesso'] = True
    return render(request , "inscrever.html" , contexto)