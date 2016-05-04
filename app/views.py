import json
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
        g.tentativas = json_data["tentativas"]
        g.frustrado = json_data["frustrado"]
        g.save()
        for i in json_data["toques"]:
            t = Toques()
            t.x = i["x"]
            t.y = i["y"]
            t.t = i["t"]
            t.save()
            g.toques.add(t)
        return HttpResponse(json_data)
		
def get_aluno(request):
    jogo = Jogo.objects.latest('aluno')
    print jogo.aluno
    return HttpResponse(jogo.aluno)
