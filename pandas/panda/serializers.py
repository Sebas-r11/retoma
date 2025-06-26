from rest_framework import serializers
from .models import produccion
import pandas as pd

class est_produccion_Serializer(serializers.ModelSerializer):
    
    class Meta: 
        model = produccion
        template_name = 'pamda/lista.html'
        context_object_name = 'object_list'
        fields = '__all__'
        
    # class Meta:
    #     model:produccion
    #     fields = ['id','seccion','dia','produccion']

    def df_serializer():
        #para obtener los datos
        queryset = produccion.objects.all()

        #serializar
        serializer = est_produccion_Serializer(queryset, many = True)

        #crear el df
        df = pd.DataFrame(serializer.data)

        return df