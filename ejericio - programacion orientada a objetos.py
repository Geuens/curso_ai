from abc import ABC, abstractmethod


class ContenidoMultimedia:
    def __init__(self, titulo, duracion, director):
        self.titulo = titulo
        self.duracion = duracion
        self.director = director

    def mostrar_informacion(self):
        print(f'Título: {self.titulo}')
        print(f'Duración: {self.duracion} minutos')
        print(f'Director: {self.director}')

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
    
    @abstractmethod
    def informar_tipo_contenido(self):
        pass


class Documental(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, tema_principal):
        super().__init__(titulo, duracion, director)
        self.tema_principal = tema_principal

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tema Principal: {self.tema_principal}')
    
    def informar_tipo_contenido(self):
        return "Este contenido multimadia es un documental."


class Pelicula(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, genero):
        super().__init__(titulo, duracion, director)
        self.genero = genero

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Género: {self.genero}')
    
    def informar_tipo_contenido(self):
        return "Este contenido multimadia es una pelicula."


class SerieTV(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, num_temporadas, num_episodios):
        super().__init__(titulo, duracion, director)
        self.num_temporadas = num_temporadas
        self.num_episodios = num_episodios

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Número de Temporadas: {self.num_temporadas}')
        print(f'Número de episodios: {self.num_episodios}')
    
    def informar_tipo_contenido(self):
        return "Este contenido multimadia es una serie de TV"


class Animacion(ContenidoMultimedia):
    def __init__(self, titulo, duracion, director, estudio_animacion):
        super().__init__(titulo, duracion, director)
        self.estudio_animacion = estudio_animacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Estudio de Animación: {self.estudio_animacion}')
    
    def informar_tipo_contenido(self):
        return"Este contenido multimadia es una pelicula de Animacion."


# Ejemplo de uso
documental = Documental("Planet Earth", 120, "Alguien", "Naturaleza")
documental.mostrar_informacion()
documental.reproducir()
documental.pausar()
documental.reiniciar()
documental.puntuar(7.4)
print(documental.nota)
print(documental.informar_tipo_contenido())

print("\n")

pelicula = Pelicula("Interstellar", 230, "Christopher Nolan", "Ciencia Ficción")
pelicula.mostrar_informacion()
pelicula.reproducir()

print("\n")

serie_tv = SerieTV("Breaking Bad", 45, "Alguien", 5, 120)
serie_tv.mostrar_informacion()
serie_tv.reproducir()

print("\n")

animacion = Animacion("Toy Story", 81, "Alguien", "Pixar")
animacion.mostrar_informacion()
animacion.reproducir()
