from rest_framework import serializers
from .models import ingreso

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingreso
        fields = ['id','fecha','cantidad','proveedor']