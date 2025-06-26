from rest_framework import generics
from .models import ingreso
from .serializers import IngresoSerializer

# Create your views here.
class ingresoList(generics.ListCreateAPIView):
    queryset = ingreso.objects.all()
    serializer_class = IngresoSerializer

class ingresoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ingreso.objects.all()
    serializer_class = IngresoSerializer