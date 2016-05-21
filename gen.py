from itertools import chain      

from django.core import serializers
from django.contrib.admin.utils import NestedObjects
from django.db.models.deletion import Collector

from app.models import Jogo

collector = NestedObjects(using="default") # database name
collector.collect(list(Jogo.objects.all()))
print collector.data

objects = list(chain.from_iterable(collector.data))
with open("backup_export.json", "w") as f:
    f.write(serializers.serialize("json", objects))
