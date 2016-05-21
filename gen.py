import json
from django.core import serializers
from app import models

def gera_dump(aluno, fase):
    data = serializers.serialize("json", models.Toques.objects.filter(jogo__aluno=aluno, jogo__fase=fase))
    data = json.loads(data)
    for da in data:
        da["fields"].update({"jogo" : 1})

    data = json.dumps(data)
    out = open("dumps/mymodel"+ aluno.__str__() + fase.__str__() + ".json", "w")
    out.write(data)
    out.close()

for j in range(1,9):
    for i in range(1,10):
        gera_dump(j,i)


'''from itertools import chain      

from django.core import serializers
from django.contrib.admin.utils import NestedObjects
from django.db.models.deletion import Collector

from app.models import Jogo

collector = NestedObjects(using="default") # database name
collector.collect([Jogo.objects.get(pk=1)])

objects = list(chain.from_iterable(collector.data))
with open("backup_export.json", "w") as f:
    f.write(serializers.serialize("json", objects))
'''
