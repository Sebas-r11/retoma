import pandas as pd
import matplotlib.pyplot as plt
from django.core.management.base import BaseCommand
from pandas.panda.models import produccion

class Command(BaseCommand):
    help = 'Grafica la producción total por día desde el modelo produccion'

    def handle(self, *args, **kwargs):
        # Obtener los datos de la base de datos
        qs = produccion.objects.all().values('seccion', 'dia', 'produccion')
        if not qs:
            print("No hay datos en la tabla produccion.")
            return
        df = pd.DataFrame.from_records(qs)

        # Agrupar la producción total por día
        df_grouped = df.groupby('dia')['produccion'].sum().reset_index()

        # Graficar
        plt.figure(figsize=(8, 5))
        plt.plot(df_grouped['dia'], df_grouped['produccion'], marker='o')
        plt.title('Producción Total por Día')
        plt.xlabel('Día')
        plt.ylabel('Producción Total')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()