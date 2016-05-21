from django.core import serializers
from app import models
data = serializers.serialize("json", models.Jogo.objects.filter(fase=1,aluno=1))
out = open("mymodel.json", "w")
out.write(data)
out.close()

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
