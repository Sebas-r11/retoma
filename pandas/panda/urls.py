from django.urls import path
from .views import produccion_List, produccion_Details


urlpatterns = [
    path('Create/' ,produccion_List.as_view(), name = 'produccion_list'),
    path('Detalles/<int:pk>/', produccion_Details.as_view(), name = 'Detalles_Producto')
    ]