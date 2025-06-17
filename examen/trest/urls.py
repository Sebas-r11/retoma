from django.urls import path
from .views import ListarTabTrest,leerTabTrest

urlpatterns = [
    path('crear/',ListarTabTrest.as_view(),name='crear'),#no estoy seguro de las segundas comillas
    path('detalles/<int:pk>/',leerTabTrest.as_view(),name='detalles')
    ]