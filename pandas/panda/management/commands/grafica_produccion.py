import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from django.core.management.base import BaseCommand
from panda.models import produccion

class Command(BaseCommand):
    help = 'Grafica la producción total por día y muestra promedios con numpy'

    def handle(self, *args, **kwargs):
        # Obtener los datos de la base de datos
        qs = produccion.objects.all().values('seccion', 'dia', 'produccion')
        if not qs:
            print("No hay datos en la tabla produccion.")
            return
        df = pd.DataFrame.from_records(qs)

        # Calcular el promedio de producción por sección usando numpy
        promedios = df.groupby('seccion')['produccion'].mean()
        print("\nPromedio de producción por sección:")
        for seccion, promedio in promedios.items():
            print(f"Sección {seccion}: {np.round(promedio, 2)}")

        # Graficar el promedio de producción por sección
        plt.figure(figsize=(8, 5))
        plt.bar(promedios.index, promedios.values)
        plt.title('Promedio de Producción por Sección')
        plt.xlabel('Sección')
        plt.ylabel('Producción Promedio')
        plt.tight_layout()
        plt.show()

        # Graficar la producción total por día
        df_grouped = df.groupby('dia')['produccion'].sum().reset_index()
        plt.figure(figsize=(8, 5))
        plt.plot(df_grouped['dia'], df_grouped['produccion'], marker='o')
        plt.title('Producción Total por Día')
        plt.xlabel('Día')
        plt.ylabel('Producción Total')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()