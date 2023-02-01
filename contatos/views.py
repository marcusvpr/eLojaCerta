from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhe(request, contatoId):
    contato = Contato.objects.get(id=contatoId)

    return render(request, 'contatos/detalhe.html', {
        'contato': contato
    })
