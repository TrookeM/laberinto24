# maze.py
from Laberinto import Laberinto, Habitacion, Puerta, Pared, ParedConBombas
from Bicho import Bestia, Agresivo, Perezoso

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bestias = []

    def construir_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def crear_laberinto(self):
        return Laberinto()

    def construir_habitacion(self, id_habitacion):
        habitacion = Habitacion(id_habitacion)
        habitacion.norte = self.construir_pared()
        habitacion.este = self.construir_pared()
        habitacion.sur = self.construir_pared()
        habitacion.oeste = self.construir_pared()
        return habitacion

    def generar_laberinto_2_habitaciones(self):
        laberinto = Laberinto()
        self.laberinto = laberinto
        habitacion1 = self.construir_habitacion(1)
        habitacion2 = self.construir_habitacion(2)
        puerta = self.crear_puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def crear_laberinto_2_habitaciones_fm(self):
        habitacion1 = self.construir_habitacion(1)
        habitacion2 = self.construir_habitacion(2)
        puerta = self.crear_puerta(habitacion1, habitacion2)
        laberinto = Laberinto()
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        return laberinto

    def agregar_bestia(self, bestia):
        self.bestias.append(bestia)

    def remover_bestia(self, bestia):
        self.bestias.remove(bestia)

    def crear_bestia_agresiva(self):
        bestia = Bestia(Agresivo())
        bestia.poder = 5
        return bestia

    def crear_bestia_perezosa(self):
        bestia = Bestia(Perezoso())
        bestia.poder = 1
        return bestia

    def imprimir(self):
        print("Juego")

class JuegoConBombas(Juego):
    def construir_pared(self):
        return ParedConBombas()

    def imprimir(self):
        print("JuegoConBombas")

# main.py
from Juego import Juego, JuegoConBombas

juego = Juego()
juego.laberinto = juego.crear_laberinto_2_habitaciones_fm()
juego.laberinto.entrar()

juego = Juego()
juego.laberinto = juego.crear_laberinto_2_habitaciones_fm()

juego = JuegoConBombas()
juego.laberinto = juego.crear_laberinto_2_habitaciones_fm()
juego.laberinto.entrar()
