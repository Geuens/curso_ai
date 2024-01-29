import random

canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01]

# Combinar las dos listas en un diccionario
canciones_dict = dict(zip(canciones, duraciones))

# Seleccionar las 3 canciones más largas
canciones_largas = dict(sorted(canciones_dict.items(), key=lambda x: x[1], reverse=True)[:3])

# Crear un diccionario con una selección aleatoria de canciones
canciones_aleatorias = dict(random.sample(canciones_dict.items(), k=3))

# Mostrar resultados
print("Diccionario de canciones y duraciones:")
print(canciones_dict)

print("\nLas 3 canciones más largas:")
print(canciones_largas)

print("\nSelección aleatoria de canciones:")
print(canciones_aleatorias)
