import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from django.core.management.base import BaseCommand
from panda.models import produccion

class Command(BaseCommand):
    help = 'Genera un gráfico de barras con el promedio de producción por sección desde la base de datos'

    def handle(self, *args, **kwargs):
        # Obtener los datos de la base de datos
        qs = produccion.objects.all().values('seccion', 'produccion')
        if not qs:
            print("No hay datos en la tabla produccion.")
            return
        df = pd.DataFrame.from_records(qs)

        # Calcular el promedio de producción por sección
        promedios = df.groupby('seccion')['produccion'].mean()

        # Crear gráfico de barras
        plt.figure(figsize=(8, 5))
        plt.bar(promedios.index, promedios.values, color='skyblue')
        plt.title('Promedio de Producción por Sección')
        plt.xlabel('Sección')
        plt.ylabel('Producción Promedio')
        plt.tight_layout()
        plt.show()