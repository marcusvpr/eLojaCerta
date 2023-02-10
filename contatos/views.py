from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)

    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhe(request, contatoId):
    # contato = Contato.objects.get(id=contatoId)
    contato = get_object_or_404(Contato, id=contatoId)

    if not contato.mostrar:
        # raise Http404()
        messages.add_message(
            request,
            messages.ERROR,
            'Contato não existe.'
        )
        return render(request, 'contatos/index.html')
        # return redirect('index')

    return render(request, 'contatos/detalhe.html', {
        'contato': contato
    })


def busca(request):
    # contatos = Contato.objects.all()
    # contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    termo = request.GET.get('termo')

    if termo is None or not termo:
        # raise Http404
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return render(request, 'contatos/index.html')
        # return redirect('index')

    # print(termo)
    campos = Concat('nome', Value(' '), 'sobrenome')

#    contatos = Contato.objects.order_by('-id').filter(
#        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
#        mostrar=True
#    )

    contatos = Contato.objects.annotate(nomeCompleto=campos).filter(
        Q(nomeCompleto__icontains=termo) | Q(telefone__icontains=termo)
    )

#   print(contatos.query)

    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
