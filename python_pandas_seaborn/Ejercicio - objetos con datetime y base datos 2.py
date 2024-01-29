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
    print("1. Añadir Contenido")
    print("2. Eliminar Contenido")
    print("3. Mostrar Lista de Contenidos")
    print("4. Buscar Contenido")
    print("5. Modificar metadatos")
    print("6. Reproducir contenido")
    print ("7. Puntuar contenido")
    print("8. Salir")

def añadir_pelicula(lista_peliculas):
    limpiar_consola()
    print("\nElija el tipo de contenido a añadir:")
    print("1. Película")
    print("2. Documental")
    print("3. Serie de TV")
    print("4. Animación")

    choice = input("Ingrese el número correspondiente al tipo de contenido: ")

    if choice == '1':
        tipo_contenido = Pelicula
    elif choice == '2':
        tipo_contenido = Documental
    elif choice == '3':
        tipo_contenido = SerieTV
    elif choice == '4':
        tipo_contenido = Animacion
    else:
        print("Opción inválida.")
        return

    titulo = input("\nIngrese el título del contenido: ")

    if titulo in [pelicula.titulo for pelicula in lista_peliculas]:
        print("La película está en la lista")
    else:
        metadatos_contenido(tipo_contenido, titulo, lista_peliculas)
        print("El ha sido añadido a la lista")


def metadatos_contenido(tipo_contenido, titulo, lista_peliculas):
    director = input("Ingrese el nombre del director: ")
    duracion = input("Ingrese la duración del contenido: ")
    fecha = input("Ingrese el año de lanzamiento: ")

    if tipo_contenido == Pelicula:
        genero = input("Ingrese el género de la película: ")
        nuevo_contenido = Pelicula(titulo, duracion, director, fecha, genero)
    elif tipo_contenido == Documental:
        tema_principal = input("Ingrese el tema principal del documental: ")
        nuevo_contenido = Documental(titulo, duracion, director, fecha, tema_principal)
    elif tipo_contenido == SerieTV:
        num_temporadas = input("Ingrese el número de temporadas de la serie: ")
        num_episodios = input("Ingrese el número de episodios de la serie: ")
        nuevo_contenido = SerieTV(titulo, duracion, director, fecha, num_temporadas, num_episodios)
    elif tipo_contenido == Animacion:
        estudio_animacion = input("Ingrese el estudio de animación: ")
        nuevo_contenido = Animacion(titulo, duracion, director, fecha, estudio_animacion)

    # Agregar el nuevo contenido a la lista existente
    lista_peliculas.append(nuevo_contenido)
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
    print("Lista de contenidos")
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

def puntuar_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese la película a puntuar: ")

    if nombre not in [pelicula.titulo for pelicula in lista_peliculas]:
        print("La película no está en la lista")
    else:
        
        pelicula = next((p for p in lista_peliculas if p.titulo.strip().lower() == nombre.strip().lower()), None)

        if pelicula is None:
            print("La película no está en la lista")
        else:
            nota = float(input("\nIngrese la nota de la pelicula: "))
            pelicula.puntuar(nota)
            guardar_base_datos(lista_peliculas)
        
        

def modificar_pelicula(lista_peliculas):
    limpiar_consola()
    nombre = input("\nIngrese el título del contenido a modificar: ")

    contenido = next((p for p in lista_peliculas if p.titulo.strip().lower() == nombre.strip().lower()), None)

    if contenido is None:
        print("El contenido no está en la lista")
        return

    else:
        lista_peliculas = [p for p in lista_peliculas if p.titulo.strip().lower() != nombre.strip().lower()]

        print("\nElija el tipo de contenido a modificar:")
        print("1. Película")
        print("2. Documental")
        print("3. Serie de TV")
        print("4. Animación")

        choice = input("Ingrese el número correspondiente al tipo de contenido: ")

        if choice == '1':
            tipo_contenido = Pelicula
        elif choice == '2':
            tipo_contenido = Documental
        elif choice == '3':
            tipo_contenido = SerieTV
        elif choice == '4':
            tipo_contenido = Animacion
        else:
            print("Opción inválida.")
            return
        
        metadatos_contenido(tipo_contenido, nombre, lista_peliculas)
        print("El contenido ha sido modificado en la lista")


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
            puntuar_pelicula(lista_peliculas)
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")