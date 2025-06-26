from rest_framework import serializers
from .models import calificador

class calificadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = calificador
        fields = ['id','proveedor','muestra','aprovados','rechazados']