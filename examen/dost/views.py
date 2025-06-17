from django.shortcuts import render
from rest_framework import generics
from .models import tabdos
from .serializers import TabdosSerializer

class ListarTabdos(generics.ListCreateAPIView):
    queryset = tabdos.objects.all()
    serializer_class = TabdosSerializer
    
class leerTabdos(generics.RetrieveUpdateDestroyAPIView):
    queryset = tabdos.objects.all()
    serializer_class = TabdosSerializer