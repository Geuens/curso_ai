import pandas as pd

# 1. Crear una Serie de Pandas a partir de una lista de números.
lista_numeros = [1, 2, 3, 4, 5]
serie = pd.Series(lista_numeros)

# 2. Mostrar la Serie.
print("Serie original:")
print(serie)


# 5. Realizar operaciones aritméticas básicas en toda la Serie.

numero = 2

suma_resultado = serie + numero
resta_resultado = serie - numero
multiplicacion_resultado = serie * numero
division_resultado = serie / numero

# 6. Mostrar los resultados de cada operación.
print("\nResultados de operaciones aritméticas:")
print("Suma:")
print(suma_resultado)
print("\nResta:")
print(resta_resultado)
print("\nMultiplicación:")
print(multiplicacion_resultado)
print("\nDivisión:")
print(division_resultado)