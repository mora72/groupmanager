from django.shortcuts import render, get_object_or_404, redirect
from .models import Grupo, Integrante, Uf
from .forms import GrupoForm, GrupoFormEdit, IntegranteForm, IntegranteFormEdit
from .modulosgroup import calcula_distancia
from django.contrib import messages


def grupo_list(request):
    searchgrupo = request.GET.get('searchgrupo')  # usa o name="search" informado no input do grupos.html
    filteruf = request.GET.get('filteruf')
    if type(filteruf) is str:
        filteruf = int(filteruf)
    base_ufs = Uf.objects.all()
    lista_grupos = Grupo.objects.all().order_by('nome')
    if searchgrupo:
        lista_grupos = lista_grupos.filter(nome__icontains=searchgrupo).order_by('nome')
    if filteruf:
        if filteruf != 0:
            lista_grupos = lista_grupos.filter(uf=filteruf).order_by('nome')
    return render(request, 'core/grupos.html', {'listagrupos': lista_grupos, 'filterufatual': filteruf,
                                                'listaufs': base_ufs})


def grupo_view(request, idgrupo):
    grupo = get_object_or_404(Grupo, pk=idgrupo)
    form = GrupoForm(instance=grupo)
    return render(request, 'core/grupoview.html', {'form': form, 'grupo': grupo})


def grupo_delete(request, idgrupo):
    grupo = get_object_or_404(Grupo, pk=idgrupo)
    grupo.delete()

    messages.info(request, f'Grupo "{grupo.nome}" removida com Sucesso !')

    return redirect('/')


def grupo_new(request):
    if request.method == 'POST':
        form = GrupoFormEdit(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            return redirect('/')
        else:
            return render(request, 'core/gruponew.html', {'form': form})
    else:
        form = GrupoFormEdit()
        return render(request, 'core/gruponew.html', {'form': form})


def grupo_edit(request, idgrupo):
    grupo = get_object_or_404(Grupo, pk=idgrupo)
    form = GrupoFormEdit(instance=grupo)

    if request.method == 'POST':
        form = GrupoFormEdit(request.POST, instance=grupo)

        if form.is_valid():
            grupo.save()
            return redirect('/')
        else:
            return render(request, 'core/grupoedit.html', {'form': form, 'grupo': grupo})
    else:
        return render(request, 'core/grupoedit.html', {'form': form, 'grupo': grupo})


def integrante_list(request):
    searchintegrante = request.GET.get('searchintegrante')  # usa o name="search" informado no input do integrante.html
    filterstatus = request.GET.get('filterstatus')
    filtergrupo = request.GET.get('filtergrupo')
    lista_integrantes = Integrante.objects.all().order_by('nome')

    if type(filtergrupo) is str:
        filtergrupo = int(filtergrupo)

    if searchintegrante:
        lista_integrantes = lista_integrantes.filter(nome__icontains=searchintegrante)

    if filterstatus and filterstatus != '*':
        lista_integrantes = lista_integrantes.filter(status=filterstatus)

    if filtergrupo and filtergrupo != 0:
        lista_integrantes = lista_integrantes.filter(grupo=filtergrupo)

    lista_grupos = Grupo.objects.all().order_by('nome')
    return render(request, 'core/integrantes.html', {'listaintegrantes': lista_integrantes,
                                                     'filterstatusatual': filterstatus,
                                                     'listagrupos': lista_grupos,
                                                     'filtergrupoatual': filtergrupo})


def integrante_view(request, idintegrante):
    integrante = get_object_or_404(Integrante, pk=idintegrante)
    form = IntegranteForm(instance=integrante)
    return render(request, 'core/integranteview.html', {'form': form, 'integrante': integrante})


def integrante_delete(request, idintegrante):
    integrante = get_object_or_404(Integrante, pk=idintegrante)
    integrante.delete()

    messages.info(request, f'Integrante "{integrante.nome}" removido com Sucesso !')

    return redirect('/integrantes/')


def integrante_new(request):
    if request.method == 'POST':
        form = IntegranteFormEdit(request.POST, request.FILES)
        if form.is_valid():
            integrante = form.save(commit=False)
            integrante.save()
            return redirect('/integrantes/')
    else:
        form = IntegranteFormEdit()
        return render(request, 'core/integrantenew.html', {'form': form})


def integrante_edit(request, idintegrante):
    integrante = get_object_or_404(Integrante, pk=idintegrante)
    form = IntegranteFormEdit(instance=integrante)

    if request.method == 'POST':
        form = IntegranteFormEdit(request.POST, request.FILES, instance=integrante)

        if form.is_valid():
            print(integrante.foto)
            integrante.save()
            print(integrante.foto)
            return redirect('/integrantes/')
        else:
            return render(request, 'core/integranteedit.html', {'form': form, 'integrante': integrante})
    else:
        return render(request, 'core/integranteedit.html', {'form': form, 'integrante': integrante})


def distancias(request):
    cidade_interesse = request.GET.get('searchcidadeinteresse')  # usa a cidade informado no input do distancias.html
    lista_distancias = []
    if cidade_interesse:
        lista_distancias = calcula_distancia(cidade_interesse.strip().upper())
    return render(request, 'core/distancias.html', {'listadistancias': lista_distancias,
                                                    'cidadeinteresse': cidade_interesse})
