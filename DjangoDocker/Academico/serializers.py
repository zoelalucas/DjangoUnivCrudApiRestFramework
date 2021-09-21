from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('url', 'codigo', 'nombre', 'creditos')