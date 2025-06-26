# Importamos la función path para definir rutas y las vistas que usaremos
from django.urls import path
from .views import produccion_List, produccion_Details, ProduccionCreateView

# Definimos las rutas (endpoints) de la app panda
urlpatterns = [
    # Ruta para la API que lista y crea producciones (JSON, no HTML)
    path('Create/', produccion_List.as_view(), name='produccion_list'),
    # Ruta para la API que muestra, actualiza o elimina una producción específica (JSON, no HTML)
    path('Detalles/<int:pk>/', produccion_Details.as_view(), name='Detalles_Producto'),
    # Ruta para mostrar el formulario HTML y crear una producción usando la vista genérica de Django
    path('nuevo/', ProduccionCreateView.as_view(), name='produccion_form'),
]