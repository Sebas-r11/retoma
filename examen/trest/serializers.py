from rest_framework import serializers
from .models import TabTrest

class TabTrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabTrest
        fields =['id','autor','texto','fecha_creacion','post_id']