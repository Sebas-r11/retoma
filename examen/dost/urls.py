from django.urls import path
from .views import ListarTabdos,leerTabdos

urlpatterns = [
    path('crear/',ListarTabdos.as_view(),name='crear'),#no estoy seguro de las segundas comillas
    path('detalles/<int:pk>/',leerTabdos.as_view(),name='detalles')
    ]