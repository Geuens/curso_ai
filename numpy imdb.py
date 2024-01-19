import pandas as pd
import numpy as np

dataset = pd.read_csv("IMDB-Movie-Data.csv")
print(dataset)
print(dataset.info())

import matplotlib.pyplot as plt

# Seleccionar columnas relevantes
selected_columns = ['Title', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']
selected_data = dataset[selected_columns]

# Convertir a un array de Numpy
numpy_array = selected_data.to_numpy()

# Manejar valores faltantes en 'Revenue (Millions)' , sustituir los valores nan me daba un error
column_to_handle = numpy_array[:, 5]
numeric_column = pd.to_numeric(column_to_handle, errors='coerce')
mean_revenue = np.nanmean(numeric_column)
column_to_handle[np.isnan(numeric_column)] = mean_revenue

# Calcular la calificación promedio de las películas
average_rating = np.mean(numpy_array[:, 3])
print("Calificacion media")
print(average_rating)
print("\n")

# Encontrar la película con la duración más larga
longest_movie_index = np.argmax(numpy_array[:, 2])
longest_movie_title = numpy_array[longest_movie_index, 0]
longest_movie_minutes = numpy_array[longest_movie_index, 2]
print("pelicula mas larga")
print(f"{longest_movie_title} con {longest_movie_minutes} minutos")
print("\n")


# Determinar el ingreso promedio y la mediana de los ingresos de las películas
average_revenue = np.mean(numpy_array[:, 5])
median_revenue = np.median(numpy_array[:, 5])

print("Ingresos medios")
print(average_revenue)
print("\n")

print("Ingreso mediano")
print(median_revenue)
print("\n")

# Crear un subconjunto de datos con películas lanzadas en los últimos 10 años
recent_movies = numpy_array[numpy_array[:, 1] >= (np.max(numpy_array[:, 1]) - 10)]

# Calcular el promedio de votos para este subconjunto
average_votes_recent_movies = np.mean(recent_movies[:, 4])

# Calcular la correlación entre la calificación de IMDb y los ingresos
column_3 = np.nan_to_num(numpy_array[:, 3].astype(float))
column_5 = np.nan_to_num(numpy_array[:, 5].astype(float))
correlation = np.corrcoef(column_3, column_5)[0, 1]
print(correlation)

# Representar la correlación con matplotlib.pyplot
plt.scatter(numpy_array[:, 3], numpy_array[:, 5])
plt.xlabel('IMDb Rating')
plt.ylabel('Ingresos')
plt.title('Correlación entre IMDb Rating e Ingresos')
plt.show()
