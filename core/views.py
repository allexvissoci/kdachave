from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from registro.models import atrasados, devolvidos, nao_devolvidos
from molho.models import Molho


@login_required
def registro_filter(request):
    filtro = request.POST.get('filter_by')
    template_name = 'tabela.html'

    if filtro not in ['atrasados', 'adevolder', 'devolvidos']:
        return Http404
    if filtro == 'atrasados':
        registros = atrasados()
    elif filtro == 'adevolder':
        registros = nao_devolvidos()
    elif filtro == 'devolvidos':
        registros = devolvidos()

    context = {
                'registros': registros
            }
    return render(request, template_name, context)


@login_required
def index(request):
    template_name = 'index2.html'
    context = {
        'atrasados': atrasados(),
        'devolvidos': devolvidos(),
        'nao_devolvidos': nao_devolvidos(),
    }
    return render(request, template_name, context)


@login_required
def updateDashboard(request):

    countEmUso = Molho.objects.filter(status=0).count()
    countDevolvidos = Molho.objects.filter(status=1).count()
    countAlerta = Molho.objects.filter(status=2).count()
    countPerdido = Molho.objects.filter(status=3).count()

    context = {
        'countEmUso': countEmUso,
        'countDevolvidos': countDevolvidos,
        'countAlerta': countAlerta,
        'countPerdido': countPerdido,
    }

    return render(request, "dashboard_molhos.html", context)
