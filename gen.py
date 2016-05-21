from itertools import chain      

from django.core import serializers
from django.contrib.admin.util import NestedObjects
from django.db.models.deletion import Collector

from app.models import Jogo

collector = NestedObjects(using="apolito") # database name
collector.collect(Jogo.objects.all())

objects = list(chain.from_iterable(collector.data))
with open("backup_export.json", "w") as f:
    f.write(serializers.serialize("json", objects))
