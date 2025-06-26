from rest_framework import generics
from .models import calificador
from .serializers import calificadorSerializer

class calificadorList(generics.ListCreateAPIView):
    queryset = calificador.objects.all()
    serializer_class = calificadorSerializer

class calificadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = calificador.objects.all()
    serializer_class = calificadorSerializer
