import platform
import os

#Inicializacion
lista_peliculas = {}

def limpiar_consola():
 
    os.system('cls')

def metadatos_pelicula(nombre):
        
        director = input("Ingrese el nombre del director: ")
        año = input("Ingrese el año de lanzamiento: ")
        presupuesto = input("Ingrese el presupuesto de la película: ")

        lista_peliculas[nombre] = {
            'Director': director,
            'Año': año,
            'Presupuesto': presupuesto
        }

def mostrar_menu():
    
    print("\n=== Menú ===")
    print("1. Añadir Película")
    print("2. Eliminar Película")
    print("3. Mostrar Lista de Películas")
    print("4. Buscar Película")
    print("5. Salir")

def añadir_pelicula(lista_peliculas):

    limpiar_consola()

    pelicula = input("\nIngrese la pelicula a añadir: ")

    if pelicula in lista_peliculas:
        print("La pelicula ya esta en la lista")
    else:
        metadatos_pelicula(pelicula)
        print("la pelicula ha sido añadida a la lista")

def eliminar_pelicula(lista_peliculas):

    limpiar_consola()

    pelicula = input("\nIngrese la pelicula a añadir: ")

    if pelicula is not lista_peliculas:
        print("La pelicula no esta en la lista")
    else:
        lista_peliculas.remove(pelicula)
        print("la pelicula ha sido eliminada de la lista")

def mostrar_peliculas(lista_peliculas):

    limpiar_consola()

    print("lista peliculas")
    for pelicula in lista_peliculas:
        print(pelicula)

def buscar_pelicula(lista_peliculas):

    limpiar_consola()

    pelicula = input("\nIngrese la pelicula a buscar: ")
    
    if pelicula is not lista_peliculas:
        print("La pelicula no esta en la lista")
    else:
        print("la pelicula esta en la lista")

def modificar_pelicula(lista_peliculas):

    limpiar_consola()

    pelicula = input("\nIngrese la pelicula a modificar: ")
    
    if pelicula is not lista_peliculas:
        print("La pelicula no esta en la lista")
    else:
        metadatos_pelicula(pelicula)
        


while (1):

    mostrar_menu()
    opcion = input("\nIngrese el número de la opción deseada: ")
        
    if opcion == '1':
        añadir_pelicula(lista_peliculas)
    elif opcion == '2':
        eliminar_pelicula(lista_peliculas)
    elif opcion == '3':
        mostrar_peliculas(lista_peliculas)
    elif opcion == '4':
        buscar_pelicula(lista_peliculas)
    elif opcion == 5:
        modificar_pelicula(lista_peliculas)
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

