from rest_framework import serializers
from .models import tabdos

class TabdosSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabdos
        fields =['id','nombre_usuario','correo_electronico','password','fecha_creacion']