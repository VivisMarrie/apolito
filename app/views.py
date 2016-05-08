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
    jogos = Jogo.objects.all()
    jsn = []
    for j in jogos:
        print j.fase
        jsn.append([j.fase, j.aluno, j.frustrado, j.tentativas, j.tempo])
    print jsn
    arff.dump('result.arff', jsn, relation="jogos", names=['fase', 'aluno', 'frustrado', 'tentativas', 'tempo'])
    return HttpResponse(jsn)
