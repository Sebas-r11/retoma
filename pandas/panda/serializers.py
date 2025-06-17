from rest_framework import serializers
from .models import produccion

class est_produccion_Serializer(serializers.ModelSerializer):
    
    class Meta: 
        model = produccion
        fields = '__all__'
        
    # class Meta:
    #     model:produccion
    #     fields = ['id','seccion','dia','produccion']