

# Crea una tupla e intenta modificar su contenido
mi_tupla = (1, 2, 3)

try:
    # Intenta modificar la tupla
    mi_tupla[0] = 5

except TypeError as e:
    # Captura el error TypeError y muestra un mensaje
    print(f"Error: {e}")

 # Creamos una tupla mixta. Recuerda que una tupla es inmutable y puede contener otro tipos dedatos como listas, cadenas, enteros, etc.
tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

# Pregunta podríamos modificar el contenido del tercer elemento tupla_mixta[2]? Escribe elcódigo necesario e inténtalo. Luego imprime la tupla y observa si ha funcionado o no.
try:
    # Intenta modificar la tupla
    tupla_mixta[2] = "modificado"

except TypeError as e:
    # Captura el error TypeError y muestra un mensaje
    print(f"Error: {e}")

print(tupla_mixta)

# Imprime los elementos de la tupla con un loop for y su tipo
# Ejemplo 1 => <class 'int'>
# dos => <class 'str'>
# Para concatenar el valor del elemento con su tipo tendremos que hacer casting de ambos con str() o usar un fstring

for elemento in mi_tupla:
    print(f"{elemento} => {type(elemento)}")

lista_mixta = list(tupla_mixta)

# Modificar el elemento 1 de la lista
lista_mixta[1] = "modificado"

# Volver a convertir la lista a una tupla
tupla_modificada = tuple(lista_mixta)

# Paso 4: Imprimir la tupla modificada
print(tupla_modificada)

#Crear una tupla numérica
tupla_numerica = (2, 4, 6, 8, 10)

# Realizar operaciones en la tupla numérica
suma_tupla = sum(tupla_numerica)
maximo_tupla = max(tupla_numerica)
minimo_tupla = min(tupla_numerica)

# Calcular los cuadrados de la tupla con compresión de listas
cuadrados_tupla = [x**2 for x in tupla_numerica]

# Desempaquetar la tupla en tantas variables como elementos tenga
elemento1, elemento2, elemento3, elemento4, elemento5 = tupla_numerica

# Imprimir resultados
print("\nOperaciones en la tupla numérica:")
print(suma_tupla)
print(maximo_tupla)
print(minimo_tupla)

print("\nCuadrados de la tupla:")
print(cuadrados_tupla)

print("\nDesempaquetado de la tupla:")
print(elemento1, elemento2, elemento3, elemento4, elemento5)