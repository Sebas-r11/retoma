from rest_framework import generics
from .models import produccion
from .serializers import est_produccion_Serializer

class produccion_List(generics.ListCreateAPIView):
    queryset = produccion.objects.all()
    serializer_class = est_produccion_Serializer

class produccion_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = produccion.objects.all()
    serializer_class = est_produccion_Serializer




