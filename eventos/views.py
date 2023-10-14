from django.shortcuts import render , get_object_or_404

from eventos.models import Evento
from eventos.forms import InscricaoEventoForm

def eventos_detalhes(request, id):
    evento = get_object_or_404(Evento, id = id)
    form = InscricaoEventoForm(request.POST or None)
    if form.is_valid():
        inscricao = form.save(commit=False)  
        inscricao.evento = evento
        inscricao.save()
        sucesso = True
    else:
        sucesso = False
    contexto = {
        'evento':evento,
        'form': form,
        'sucesso': sucesso,
        
    }
    return render(request ,'evento.html',contexto)