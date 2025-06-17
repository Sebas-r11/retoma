from django.urls import path
from .views import ListarExamen,leerExamen

urlpatterns = [
    path('crear/',ListarExamen.as_view(),name='crear'),#no estoy seguro de las segundas comillas
    path('detalles/<int:pk>/',leerExamen.as_view(),name='detalles')
    ]