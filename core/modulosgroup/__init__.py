from ..models import Grupo, Distancia
from operator import itemgetter
from ..distcalcmodule import *


def get_distances(origem, cidade_destino, uf_destino, lista_dist_atuais):
    dist = 0
    for x in lista_dist_atuais:
        if x.origem == origem and x.cidade_destino == cidade_destino and x.uf_destino == uf_destino:
            dist = x.distancia
            break
    return dist


def calcula_distancia(cidade_busca):
    lista_grupos = Grupo.objects.all()
    lista_dist_calc = {}
    lista_grupo_cidade ={}
    lista_grupo_uf ={}
    lista_dist_atuais = Distancia.objects.all()
    for x in lista_grupos:
        dist = get_distances(cidade_busca, x.cidade, x.uf, lista_dist_atuais)
        if dist == 0:
            origem = f'{cidade_busca}'
            destino = f'{x.cidade}, {x.uf}'
            dist = gmaps_distances(origem, destino)
            new_distancia = Distancia(origem=cidade_busca, cidade_destino=x.cidade, uf_destino=x.uf, distancia=dist)
            new_distancia.save()  # salva no DB a nova distância calculada
        lista_dist_calc[x.nome] = dist
        lista_grupo_cidade[x.nome] = x.cidade
        lista_grupo_uf[x.nome] = x.uf.uf
    lista_dist_sorted = sorted(lista_dist_calc.items(), key=itemgetter(1))
    lista_dist_retorno = []
    for x in lista_dist_sorted:
        registro = {'grupo': x[0], 'dist': x[1], 'cidade': lista_grupo_cidade[x[0]], 'uf': lista_grupo_uf[x[0]]}
        lista_dist_retorno.append(registro.copy())
    print(lista_dist_retorno)
    return lista_dist_retorno
