import pandas as pd
import sqlite3
import os

# 1. Leer datos desde un archivo CSV (tener 'produccion_data.csv' en la misma carpeta)
if not os.path.exists('produccion_data.csv'):
    print('No se encontró el archivo produccion_data.csv')
    exit(1)
    

df = pd.read_csv('produccion_data.csv')
print('Datos cargados:')
print(df.head())

# 2. Procesar datos: ejemplo, sumar la producción por sección
df_resumen = df.groupby('seccion')['produccion'].sum().reset_index()
print('\nProducción total por sección:')
print(df_resumen)

# 3. Guardar el resumen en una base de datos SQLite
conn = sqlite3.connect('produccion.db')
df_resumen.to_sql('resumen_produccion', conn, if_exists='replace', index=False)
print('\nResumen guardado en la base de datos produccion.db (tabla resumen_produccion)')

# 4. Cerrar la conexión a la base de datos
conn.close()
print('\nProceso finalizado.')
