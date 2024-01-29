import requests
from dotenv import load_dotenv
import os
from PIL import Image, ImageTk
import tkinter as tk
#import matplotlib
import io
# Cargar variables de entorno desde .env
load_dotenv()

url_omdb = "http://www.omdbapi.com/?apikey=" + os.getenv("OMDB_API_KEY") + "&t="


def get_poster(movie):
    """ 
    Devuelve la ruta al poster en jpg
    
    Args:
        imdbId (str): El identificador IBMDB de la película
    """
    result = requests.get(url_omdb + movie)
    result_json = result.json()
    return result_json["Poster"]


def show_poster(url, ventana):
    # Obtener la imagen de la URL
    respuesta = requests.get(url)
    imagen = Image.open(io.BytesIO(respuesta.content))

    # Convertir la imagen para Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget de etiqueta (Label) y asignarle la imagen
    etiqueta = tk.Label(ventana, image=imagen_tk)
    etiqueta.image = imagen_tk  # Mantener una referencia
    etiqueta.pack()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Visualizador de Imágenes")


show_poster(get_poster('The Godfather'), ventana_principal)
show_poster(get_poster('Avatar'), ventana_principal)

ventana_principal.mainloop()


def get_ratings(movie):

    result = requests.get(url_omdb + movie)
    result_json = result.json()
    return result_json["Ratings"]

def show_ratings(ratings, ventana):

    for rating in ratings:
        print(f"{rating['Source']}: {rating['Value']}")


movie_ratings = get_ratings('Avatar')
show_ratings(movie_ratings, ventana_principal)

ventana_principal.mainloop()