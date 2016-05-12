import json, arff
from app.models import Toques, Jogo
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt


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
            t.save()
            g.toques.add(t)
        return HttpResponse(json_data)
		
def get_aluno(request):
    jogo = Jogo.objects.latest('aluno')
    print jogo.aluno
    return HttpResponse(jogo.aluno)
    
def generate_data(request):
    generate_arquivo(1)
    generate_arquivo(2)
    generate_arquivo(3)
    generate_arquivo(4)
    generate_arquivo(5)
    generate_arquivo(6)

    return HttpResponse("Gerado ARFFs")


def generate_arquivo(fase):
    jogo_fase = Jogo.objects.all().filter(fase=fase)
    jsn = []
    colunas = ['aluno', 'frustrado', 'tentativas', 'tempo', 'qtd_toques']

    qtd_max_toq = 0
    for j in jogo_fase:
        toques = j.toques.all().order_by('t')
        qtd_toques = toques.count()
        if qtd_max_toq <= qtd_toques :
            qtd_max_toq = qtd_toques
        col_toq = []
        for t in toques:
            col_toq.append(t.x)
            col_toq.append(t.y)
            col_toq.append(t.t)
            col_toq.append(t.acao)
        jsn.append([j.aluno, j.frustrado, j.tentativas, j.tempo, qtd_toques] + col_toq)

    ind = 0
    for j in jogo_fase:
        toques = j.toques.all().order_by('t')
        qtd_toques = toques.count()
        for i in range(qtd_toques, qtd_max_toq):
            if qtd_toques == qtd_max_toq:
                break
            print "i:" + i.__str__()
            jsn[ind]= jsn[ind] + [0L, 0L, 0L, 0L]
        ind = + 1

    print jsn

    for i in range(1, qtd_max_toq+1):
        colunas.append('toque_' + i.__str__() + '_x')
        colunas.append('toque_' + i.__str__() + '_y')
        colunas.append('toque_' + i.__str__() + '_t')
        colunas.append('toque_' + i.__str__() + '_acao')

    arff.dump('results/result_fase_'+fase.__str__() +'.arff', jsn, relation="jogo_fase_" + fase.__str__(), names=colunas)
