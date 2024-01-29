import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Leer los datos desde el enlace proporcionado
url = "https://drive.google.com/uc?export=download&id=10JJmUmZaDE8k8AQs2gKbPZGPmrIH6GQG"
df = pd.read_csv(url)

# Mostrar las primeras filas del DataFrame para entender la estructura de los datos
df.head()

# Identificar valores faltantes o incorrectos
#msno.matrix(df)
plt.show()

# Visualizar la distribución de valores faltantes por columna
msno.bar(df)
plt.show()

# Crear un mapa de calor para visualizar la ubicación de los valores faltantes
#msno.heatmap(df)
plt.show()

# Obtener estadísticas descriptivas, incluyendo percentiles
statistics = df.describe(percentiles=[.25, .5, .75, .90, .95, .99])

# Alinear los operandos antes de realizar la comparación
df_aligned, statistics_aligned = df.align(statistics.loc['99%'], axis=1)

# Verificar si '1%' está presente en el índice
if '1%' in statistics_aligned.index:
    # Identificar outliers basándonos en percentiles
    outliers = df_aligned[
        (df_aligned > statistics_aligned).any(axis=1) |
        (df_aligned < statistics_aligned.loc['1%']).any(axis=1)
    ]
    
    # Visualizar los outliers
    print("Outliers:")
    print(outliers)
else:
    print("El percentil '1%' no está presente en las estadísticas descriptivas.")

# Visualizar la correlación entre valores faltantes en diferentes columnas
msno.dendrogram(df)
plt.show()

# Mostrar un dendrograma para revelar patrones de valores faltantes y su relación
msno.dendrogram(df, method='ward')
plt.show()

# Imputar valores faltantes (rellenar con la media en este caso)
df_imputed = df.fillna(df.mean())

# Volver a visualizar la matriz de valores faltantes después de la imputación
msno.matrix(df_imputed)
plt.show()
