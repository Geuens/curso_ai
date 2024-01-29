import pandas as pd

temperaturas = [25, 28, 30, 22, 26, 29, 24]
precipitacion = [5, 10, 2, 15, 8, 3, 12]

serie_a = pd.Series(temperaturas, name='Temperaturas (°C)')
serie_b = pd.Series(precipitacion, name='Precipitación (mm)')

# Realizar operaciones de slicing en ambas Series
sliced_a = serie_a[2:5]  
sliced_b = serie_b[1:4]  

# Combinar las Series resultantes del slicing en una nueva Serie
serie_combinada = pd.concat([sliced_a, sliced_b], axis=1)

# Realizar operaciones básicas en la Serie combinada
promedio_temperaturas = serie_combinada['Temperaturas (°C)'].mean()
total_precipitacion = serie_combinada['Precipitación (mm)'].sum()

# Imprimir los resultados
print("Serie A:\n", serie_a)
print("\nSerie B:\n", serie_b)
print("\nSlicing en Serie A:\n", sliced_a)
print("\nSlicing en Serie B:\n", sliced_b)
print("\nSerie Combinada:\n", serie_combinada)
print("\nPromedio de temperaturas en la Serie Combinada:", promedio_temperaturas)
print("Total de precipitación en la Serie Combinada:", total_precipitacion)