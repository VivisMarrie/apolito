import json, arff
from app.models import Toques, Jogo
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from itertools import chain      

from django.core import serializers
from django.contrib.admin.utils import NestedObjects
from django.db.models.deletion import Collector

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print request.body
        json_data = json.loads(request.body.decode("utf-8"))
        g = Jogo()
        g.fase = json_data["fase"]
        g.tempo = json_data["tempo"]
        g.aluno = json_data["aluno"]
        g.tentativas = json_data["tentativas"]
        g.frustrado = json_data["frustrado"]
        g.save()
        for i in json_data["toques"]:
            t = Toques()
            t.x = i["x"]
            t.y = i["y"]
            t.t = i["t"]
            t.acao = i["acao"]
            t.jogo = g
            t.save()
        return HttpResponse(json_data)
        
		
def get_aluno(request):
    jogo = Jogo.objects.latest('aluno')
    return HttpResponse(jogo.aluno)
    
def generate_data(request):
    generate_arquivo(1)
    generate_arquivo(2)
    generate_arquivo(3)
    generate_arquivo(4)
    generate_arquivo(5)
    generate_arquivo(6)
    generate_arquivo(7)    
    generate_arquivo(8)    
    generate_arquivo(9)
    print "gerado ARFFs"
    return HttpResponse("Gerado ARFFs")


def generate_arquivo(fase):
    jogo_fase = Jogo.objects.all().filter(fase=fase)
    jsn = []
    colunas = ['aluno', 'frustrado','qtd_toques', 'tentativas', 'tempo', 'med_toques_segundo']

    colunas.extend(['qtd_toque_tipo_' + x.__str__() for x in range(13)])

    qtd_max_toq = 0
    for j in jogo_fase:
        toques = j.toques_set.all().order_by('t')
        qtd_toques = toques.count()
        if qtd_max_toq <= qtd_toques :
            qtd_max_toq = qtd_toques
        col_toq = []

        qtd_toque_tipo = [0] * 13
        for t in toques:
            col_toq.append(t.x)
            col_toq.append(t.y)
            col_toq.append(t.t)
            col_toq.append(t.acao)
            qtd_toque_tipo[t.acao] = qtd_toque_tipo[t.acao] + 1

        med_toques_segundo = 0
        if float(j.tempo/100.0) <> 0:
            med_toques_segundo = qtd_toques / float(j.tempo/100.0)

        jsn.append([j.aluno, j.frustrado, qtd_toques, j.tentativas, j.tempo, med_toques_segundo] + qtd_toque_tipo + col_toq)

    ind = 0
    for j in jogo_fase:
        toques = j.toques_set.all().order_by('t')
        qtd_toques = toques.count()
        for i in range(qtd_toques, qtd_max_toq):
            if qtd_toques == qtd_max_toq:
                break
            jsn[ind] = jsn[ind] + [0L, 0L, 0L, 0L]
        ind = ind + 1

    for i in range(1, qtd_max_toq+1):
        colunas.append('toque_' + i.__str__() + '_x')
        colunas.append('toque_' + i.__str__() + '_y')
        colunas.append('toque_' + i.__str__() + '_t')
        colunas.append('toque_' + i.__str__() + '_acao')

    arff.dump('results/result_fase_'+fase.__str__() +'.arff', jsn, relation="jogo_fase_" + fase.__str__(), names=colunas)
