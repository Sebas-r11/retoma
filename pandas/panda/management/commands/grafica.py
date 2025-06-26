import pandas as pd
import matplotlib.pyplot as plt
from django.core.management.base import BaseCommand
from panda.models import produccion

class Command(BaseCommand):
    help = 'Grafica la producción total por día'

    def handle(self, *args, **kwargs):
        qs = produccion.objects.all().values('seccion', 'dia', 'produccion')
        df = pd.DataFrame.from_records(qs)
        df_grouped = df.groupby('dia')['produccion'].sum().reset_index()
        plt.plot(df_grouped['dia'], df_grouped['produccion'], marker='o')
        plt.title('Producción Total por Día')
        plt.xlabel('Día')
        plt.ylabel('Producción Total')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()