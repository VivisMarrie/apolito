from django.db import models

class Jogo(models.Model):
    fase = models.IntegerField()
    aluno = models.IntegerField()
    tempo = models.IntegerField()
    tentativas = models.IntegerField()
    frustrado = models.BooleanField()
    #toques = models.ManyToManyField(Toques)
    def __str__(self):
        return "Aluno: " + self.aluno.__str__() + ", Fase: " + self.fase.__str__()

class Toques(models.Model):
    x = models.IntegerField()  # ponto x
    y = models.IntegerField()  # ponto y
    t = models.IntegerField()  # tempo
    acao = models.IntegerField()  # qual acao sera executada nesse clique
    jogo = models.ForeignKey(Jogo)

    def __str__(self):
        return "x: " + self.x.__str__() + ", y:".__str__() + self.y.__str__() + ", t:" + self.t.__str__()

    '''{
        "fase": 1,
	"aluno": 1;
        "tempo": 100,
        "tentativas": 2,
        "toques": [
            {
                "x": 100,
                "y": 200,
                "t": 2,
		"acao" : 0
            },
            {
                "x": 500,
                "y": 300,
                "t": 6,
		"acao" : 2
            },
            {
                "x": 400,
                "y": 800,
                "t": 8,
		"acao" : 4
            }
        ],
        "frustrado": false
    }'''
