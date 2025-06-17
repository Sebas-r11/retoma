from rest_framework import serializers
from . models import examen

class seritab(serializers.ModelSerializer):
    class Meta:
        model = examen
        fields = ['id','cliente','vuelo','fecha_salida','fecha_entrada']