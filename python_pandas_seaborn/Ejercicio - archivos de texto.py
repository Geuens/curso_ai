# Intentamos abrir el archivo en modo de lectura ('r') 
try:
    with open("mi_archivo.txt", 'r', encoding='utf-8') as archivo:
        print("Ya existe el archivo")

except FileNotFoundError:
    print("No existe el archivo")

    lineas_para_escribir = [
        "Esta es la primera linea.",
        "Esta es la segunda linea.",
        "Esta es la tercera linea.",
        "Esta es la cuarta linea.",
        "Esta es la quinta linea.",
    ]

    with open("mi_archivo.txt", 'w', encoding='utf-8') as archivo:
        for linea in lineas_para_escribir:
            archivo.write(linea + '\n')

# Abrimos el archivo en modo de lectura con encoding UTF-8
with open("mi_archivo.txt", 'r', encoding='utf-8') as archivo:
    # Utilizamos un bucle para leer y mostrar cada línea del archivo
    while True:
        # Leemos una línea del archivo
        linea = archivo.readline()

        # Verificamos si la línea está vacía (fin del archivo)
        if not linea:
            break

        # Mostramos la línea y la posición actual del cursor
        print(linea.strip(), "- Posición:", archivo.tell())

# Abrimos el archivo en modo de escritura ('w') y agregamos una nueva línea de texto al final 
with open("mi_archivo.txt", 'w', encoding='utf-8') as archivo:
    archivo.write("Nueva linea de texto\n")

# Abrimos el archivo en modo de anexar ('a+') 
with open("mi_archivo.txt", 'a+', encoding='utf-8') as archivo:
    archivo.write("otra línea en modo anexar\n")

    # Usamos seek(0) para volver al inicio
    archivo.seek(0)

    # Leemos el archivo completo con file.read()
    contenido = archivo.read()
    print("Contenido del archivo después de anexar y leer:", contenido)

# en modo 'a' 
try:
    with open("mi_archivo.txt", 'a', encoding='utf-8') as archivo:
        archivo.write("añadir otra línea en modo 'a'\n")
except IOError as e:
    print(f"Error al abrir en modo 'a': {e}")
