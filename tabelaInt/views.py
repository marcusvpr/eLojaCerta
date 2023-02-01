from django.shortcuts import render
from django.views.generic.list import ListView
from . import models


class TabelaInts(ListView):
    model = models.TabelaInt
    template_name = 'tabelaInt/lista.html'
    context_object_name = 'tabelaInts'
    paginate_by = 10
    ordering = ['-id']


def detalhe(request, tabelaIntId):
    model = models.TabelaInt

    tabelaInt = models.TabelaInt.objects.get(id=tabelaIntId)

    return render(request, 'tabelaInt/detalhe.html', {
        'tabelaInt': tabelaInt
    })
