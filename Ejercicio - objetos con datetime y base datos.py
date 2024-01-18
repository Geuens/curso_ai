from abc import  abstractmethod
from datetime import datetime
import calendar
import platform
import os
import json


class ContenidoMultimedia:
    def __init__(self, titulo, duracion, director, fecha):
        self.titulo = titulo
        self.duracion = duracion
        self.director = director
        self.fecha = fecha
    

    def mostrar_informacion(self):
        print(f'Título: {self.titulo}')
        print(f'Duración: {self.duracion} minutos')
        print(f'Director: {self.director}')
        self.mostrar_fecha()
    

    def reproducir(self):
        print(f"Reproduciendo {self.titulo}.")
    
    def pausar(self):
        print(f"Pausado {self.titulo}.")
    
    def reiniciar(self):
        print(f"Pelicula {self.titulo}. reiniciada")
        self.reproducir()
    
    def puntuar(self, nota):
        if 0 <= nota <= 10:
            self.nota = nota
            print(f'Se ha puntuado la película "{self.titulo}" con un {nota}')
        else:
            print('La puntuación debe estar entre 0 y 10')
    
    def mostrar_fecha(self):

        lista_meses = list(calendar.month_name)

        if isinstance(self.fecha, datetime):
            print(f"Fecha: {self.fecha.day} {lista_meses[self.fecha.month]} {self.fecha.year}")
        else:
            print(f"Fecha: {self.fecha}")
    
    
    def to_json(self):
        data = {'titulo': self.titulo, 'duracion': self.duracion, 'director': self.director, 'fecha': self.fecha}
        attributes = ['genero', 'tema_principal', 'num_temporadas', 'num_episodios', 'estudio_animacion']
        data.update({attr: getattr(self, attr, None) for attr in attributes})
        
        # Agregar nota solo si está definido en la instancia
        if hasattr(self, 'nota'):
            data['nota'] = self.nota
        else:
            data['nota'] = None
        
        data['tipo_contenido'] = self.informar_tipo_contenido()
        return data
    
    
    @classmethod
    def from_json(cls, data):
        content_type = data.get('tipo_contenido', None)

        if content_type == 'documental':
            return Documental(**data)
        elif content_type == 'pelicula':
            return Pelicula(**data)
        elif content_type == 'serie_tv':
            return SerieTV(**data)
        elif content_type == 'animacion':
            return Animacion(**data)
        else:
            raise ValueError("Tipo de contenido desconocido")

    
    @abstractmethod
    def informar_tipo_contenido(self):
        pass


class Documental(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, fecha, tema_principal):
        super().__init__(titulo, duracion, director, fecha)
        self.tema_principal = tema_principal

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tema Principal: {self.tema_principal}')
    
    
    def informar_tipo_contenido(self):
        return "documental."


class Pelicula(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, fecha, genero):
        super().__init__(titulo, duracion, director, fecha)
        self.genero = genero

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Género: {self.genero}')
    
    def informar_tipo_contenido(self):
        return "pelicula."


class SerieTV(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, fecha, num_temporadas, num_episodios):
        super().__init__(titulo, duracion, director, fecha)
        self.num_temporadas = num_temporadas
        self.num_episodios = num_episodios

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Número de Temporadas: {self.num_temporadas}')
        print(f'Número de episodios: {self.num_episodios}')
    
    def informar_tipo_contenido(self):
        return "serie_tv"


class Animacion(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, fecha, estudio_animacion):
        super().__init__(titulo, duracion, director, fecha)
        self.estudio_animacion = estudio_animacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Estudio de Animación: {self.estudio_animacion}')
    
    def informar_tipo_contenido(self):
        return"animacion."




### Programa
def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Darwin':
        os.system('clear')
    else:
        # Assuming Linux or other platforms using ANSI escape codes
        os.system('clear')

def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Añadir Película")
    print("2. Eliminar Película")
    print("3. Mostrar Lista de Películas")
    print("4. Buscar Película")
    print("5. Modificar metadatos")
    print("6. Reproducir pelicula")
    print("7. Salir")

def añadir_pelicula(lista_peliculas ):
    limpiar_consola()
    pelicula = input("\nIngrese la película a añadir: ")

    if pelicula in [pelicula.titulo for pelicula in lista_peliculas] :
        print("La película ya está en la lista")
    else:
        metadatos_pelicula(pelicula, lista_peliculas )
        print("La película ha sido añadida a la lista")

def metadatos_pelicula(nombre, lista_peliculas ):
    director = input("Ingrese el nombre del director: ")
    duracion = input("Ingrese la duracion de la pelicula: ")
    fecha = input("Ingrese el año de lanzamiento: ")
    genero = input("Ingrese el genero de la película: ")

    nueva_pelicula = Pelicula(nombre, duracion, director, fecha, genero)

    # Agregar la nueva película al diccionario existente
    lista_peliculas.append(nueva_pelicula)
    guardar_base_datos(lista_peliculas)

def eliminar_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese la película a eliminar: ")

    if nombre not in [pelicula.titulo for pelicula in lista_peliculas]:
        print("La película no está en la lista")
    else:
        lista_peliculas = [pelicula for pelicula in lista_peliculas if pelicula.titulo.strip().lower() != nombre.strip().lower()]
        guardar_base_datos(lista_peliculas)
        print("La película ha sido eliminada de la lista")

def mostrar_peliculas(lista_peliculas):
    limpiar_consola()
    print("Lista de películas")
    print("\n")

    iterator = iter(lista_peliculas)
    try:
        while True:
            pelicula = next(iterator)
            pelicula.mostrar_informacion()
            print("\n")

    except StopIteration:
        pass

def buscar_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese la película a buscar: ")

    if nombre not in [pelicula.titulo for pelicula in lista_peliculas]:
        print("La película no está en la lista")
    else:
        print("La película está en la lista")

def reproducir_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese la película a reproducir: ")

    if nombre not in [pelicula.titulo for pelicula in lista_peliculas]:
        print("La película no está en la lista")
    else:
        
        pelicula = next((p for p in lista_peliculas if p.titulo.strip().lower() == nombre.strip().lower()), None)

        if pelicula is None:
            print("La película no está en la lista")
        else:
            pelicula.reproducir()
        
        

def modificar_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese la película a modificar: ")

    lista_peliculas = [pelicula for pelicula in lista_peliculas if pelicula.titulo.strip().lower() != nombre.strip().lower()]
    metadatos_pelicula(nombre, lista_peliculas)
    print("La película ha sido modificada")

def cargar_base_datos():
    try:
        # Intenta abrir el archivo JSON
        with open("base_datos_peliculas.json", "r") as archivo:
            base_datos = json.load(archivo)
            lista_peliculas = [Pelicula(pelicula["titulo"], pelicula["duracion"], pelicula["director"], pelicula["fecha"], pelicula["genero"]) for pelicula in base_datos["peliculas"]]

        return lista_peliculas
    
    except FileNotFoundError:
        # Si el archivo no existe, crea una base de datos vacía
        print("El archivo no existe. Creando una nueva base de datos.")
        return []

def guardar_base_datos(lista_peliculas):
    # Guarda la base de datos en el archivo JSON
    with open("base_datos_peliculas.json", "w") as archivo:
        data = [pelicula.to_json() for pelicula in lista_peliculas]
        base_datos = {"peliculas": data}
        json.dump(base_datos, archivo, indent=2)
    print("Base de datos guardada exitosamente.")

if __name__ == "__main__":
    

    while True:

        #init
        lista_peliculas = cargar_base_datos()
        mostrar_menu()
        opcion = input("\nIngrese el número de la opción deseada: ")

        if opcion == '1':
            añadir_pelicula(lista_peliculas )
        elif opcion == '2':
            eliminar_pelicula(lista_peliculas )
        elif opcion == '3':
            mostrar_peliculas(lista_peliculas )
        elif opcion == '4':
            buscar_pelicula(lista_peliculas )
        elif opcion == '5':
            modificar_pelicula(lista_peliculas )
        elif opcion == '6':
            reproducir_pelicula(lista_peliculas)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")