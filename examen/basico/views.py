from django.shortcuts import render
from rest_framework import generics
from .models import examen
from .serializers import seritab

class ListarExamen(generics.ListCreateAPIView):
    queryset = examen.objects.all()
    serializer_class = seritab

class leerExamen(generics.RetrieveUpdateDestroyAPIView):
    queryset = examen.objects.all()
    serializer_class = seritab