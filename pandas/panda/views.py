from rest_framework import generics
from .models import produccion
from .serializers import est_produccion_Serializer
# Importamos la vista genérica CreateView de Django para manejar formularios HTML automáticamente
from django.views.generic.edit import CreateView

# Vista de API para listar y crear producciones (JSON, no HTML)
class produccion_List(generics.ListCreateAPIView):
    # Definimos el conjunto de datos que usará la vista (todas las producciones)
    queryset = produccion.objects.all()
    # Definimos el serializador que convierte los datos a JSON
    serializer_class = est_produccion_Serializer

# Vista de API para ver, actualizar o eliminar una producción específica (JSON, no HTML)
class produccion_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = produccion.objects.all()
    serializer_class = est_produccion_Serializer

# Vista genérica de Django para mostrar un formulario HTML y crear una producción
# Esta vista se encarga de mostrar el formulario, validar y guardar el objeto automáticamente
class ProduccionCreateView(CreateView):
    model = produccion  # Modelo que se va a crear
    fields = ['seccion', 'produccion']  # Campos que aparecerán en el formulario
    template_name = 'panda/formulario.html'  # Template HTML que se usará para el formulario
    success_url = '/sup/'  # URL a la que se redirige después de guardar correctamente




