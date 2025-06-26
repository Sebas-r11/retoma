import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from django.core.management.base import BaseCommand
from panda.models import produccion

class Command(BaseCommand):
    help = 'Genera un gráfico polar con el promedio de producción por sección desde la base de datos'

    def handle(self, *args, **kwargs):
        # Obtener los datos de la base de datos
        qs = produccion.objects.all().values('seccion', 'produccion')
        if not qs:
            print("No hay datos en la tabla produccion.")
            return
        df = pd.DataFrame.from_records(qs)

        # Calcular el promedio de producción por sección
        promedios = df.groupby('seccion')['produccion'].mean()

        # Preparar datos para gráfico polar
        categorias = promedios.index.tolist()
        valores = promedios.values.tolist()

        # Convertir los valores y ángulos
        valores += valores[:1]  # cerrar el gráfico
        angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
        angulos += angulos[:1]

        # Crear gráfico polar
        plt.figure(figsize=(6,6))
        ax = plt.subplot(111, polar=True)
        ax.plot(angulos, valores, 'o-', linewidth=2)
        ax.fill(angulos, valores, alpha=0.25)

        ax.set_xticks(angulos[:-1])
        ax.set_xticklabels(categorias)
        plt.title("Promedio de Producción por Sección (Gráfico Polar)")
        plt.show()