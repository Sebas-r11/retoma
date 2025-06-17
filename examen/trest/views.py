from django.shortcuts import render
from rest_framework import generics
from .models import TabTrest
from .serializers import TabTrestSerializer

class ListarTabTrest(generics.ListCreateAPIView):
    queryset = TabTrest.objects.all()
    serializer_class = TabTrestSerializer

class leerTabTrest(generics.RetrieveUpdateDestroyAPIView):
    queryset = TabTrest.objects.all()
    serializer_class = TabTrestSerializer