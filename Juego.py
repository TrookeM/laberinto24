from Laberinto import Laberinto, Habitacion, Puerta, Pared, ParedConBomba, Bomba, Norte, Este, Sur, Oeste, Noreste, Sureste, Suroeste, Noroeste
from Bicho import Bestia, Modo, Agresiva, Perezosa, Persona
from ThreadManager import ThreadManager
import copy
import time

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bestias = []
        self.persona = None
        self.prototipo = None
        self.gestorDeHilos = ThreadManager()
    
    def obtenerHabitacion(self, id):
        return self.laberinto.obtenerHabitacion(id)

    def iniciarHilos(self):
        print("Las bestias comienzan a moverse...")
        for bestia in self.bestias:
            self.gestorDeHilos.agregarHilo(bestia)
        self.gestorDeHilos.iniciar()

    def detenerHilos(self):
        print("Las bestias están detenidas...")
        for bestia in self.bestias:
            bestia.vida = 0

    def hacerPared(self):
        return Pared()
    
    def hacerPuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def hacerHabitacion(self, identificador):
        habitacion = Habitacion(identificador)
        habitacion.agregarOrientacion(self.hacerNorte())
        habitacion.agregarOrientacion(self.hacerEste())
        habitacion.agregarOrientacion(self.hacerSur())
        habitacion.agregarOrientacion(self.hacerOeste())
        habitacion.norte = self.hacerPared()
        habitacion.este = self.hacerPared()
        habitacion.sur = self.hacerPared()
        habitacion.oeste = self.hacerPared()
        return habitacion

    def hacerNorte(self):
        return Norte().obtener_instancia()

    def hacerEste(self):
        return Este.obtener_instancia()
    
    def hacerSur(self):
        return Sur().obtener_instancia()
    
    def hacerOeste(self):
        return Oeste().obtener_instancia()
    
    def hacerSureste(self):
        return Sureste().obtener_instancia()

    def hacerSuroeste(self):
        return Suroeste().obtener_instancia()

    def hacerNoreste(self):
        return Noreste().obtener_instancia()

    def hacerNoroeste(self):
        return Noroeste().obtener_instancia()
      
    def crearLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        self.laberinto = laberinto
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)

        puerta = Puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta  
        habitacion2.norte = puerta

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)

    def crear4Habitaciones4BestiasFM(self):
        habitacion1 = self.hacerHabitacion(1)
        habitacion2 = self.hacerHabitacion(2)
        habitacion3 = self.hacerHabitacion(3)
        habitacion4 = self.hacerHabitacion(4)
        
        puerta12 = self.hacerPuerta(habitacion1, habitacion2)
        puerta13 = self.hacerPuerta(habitacion1, habitacion3)
        puerta24 = self.hacerPuerta(habitacion2, habitacion4)
        puerta34 = self.hacerPuerta(habitacion3, habitacion4)
        
        habitacion1.sur = puerta12
        habitacion2.norte = puerta12
        
        habitacion1.este = puerta13
        habitacion3.oeste = puerta13
        
        habitacion2.este = puerta24
        habitacion4.oeste = puerta24
        
        habitacion3.sur = puerta34
        habitacion4.norte = puerta34
        
        laberinto = Laberinto()
                
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        laberinto.agregarHabitacion(habitacion3)
        laberinto.agregarHabitacion(habitacion4)
        self.laberinto = laberinto

        bestia1 = self.hacerBestiaAgresiva(habitacion1)
        bestia2 = self.hacerBestiaPerezosa(habitacion2)  
        bestia3 = self.hacerBestiaAgresiva(habitacion3)
        bestia4 = self.hacerBestiaPerezosa(habitacion4)
       
        self.agregarBestia(bestia1)
        self.agregarBestia(bestia2)
        self.agregarBestia(bestia3)
        self.agregarBestia(bestia4)

        return laberinto

    def crearLaberinto2HabitacionesFM(self):
        habitacion1 = self.hacerHabitacion(1)
        habitacion2 = self.hacerHabitacion(2)
        puerta = self.hacerPuerta(habitacion1, habitacion2)
        laberinto = Laberinto()
        self.laberinto = laberinto
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
      
        habitacion1.sur = puerta 
        habitacion2.norte = puerta

        return laberinto
    
    def agregarPersona(self, nombre):
        self.persona = Persona(nombre)
        self.persona.juego = self
        self.laberinto.entrar(self.persona)

    def agregarBestia(self, bestia):
        bestia.numero = len(self.bestias) + 1
        bestia.juego = self
        self.bestias.append(bestia)        

    def eliminarBestia(self, bestia):
        self.bestias.remove(bestia)
    
    def hacerBestiaAgresiva(self, habitacion):
        bestia = Bestia(Agresiva())
        bestia.poder = 5
        bestia.posicion = habitacion
        return bestia
    
    def hacerBestiaPerezosa(self, habitacion):
        bestia = Bestia(Perezosa())
        bestia.poder = 1
        bestia.posicion = habitacion
        return bestia
    
    def encontrarPersona(self, unCont):
        if self.persona.posicion == unCont:
            return self.persona
        else:
            return None
    
    def encontrarBestia(self, unCont):
        for bestia in self.bestias:
            if bestia.posicion == unCont:
                return bestia
        else:
            return None
    
    def abrirPuertas(self):
        print("Abriendo todas las puertas...")
        abrirPuertas = lambda cada: cada.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrarPuertas(self):
        print("Cerrando todas las puertas...")
        cerrarPuertas = lambda cada: cada.cerrar()
        self.laberinto.recorrer(cerrarPuertas)
    
    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)
      

# BombedGame.py
class JuegoConBombas(Juego):
  def hacerPared(self):
    return ParedConBomba()

  def print(self):
    print("Juego con Bombas")


# Ejemplos de uso
# juego = Juego()
# juego.crearLaberinto2Habitaciones()# juego.laberinto.entrar()

# juego = Juego()
# juego.crearLaberinto2HabitacionesFM()

# juego = JuegoBombardeado()
# juego.crearLaberinto2HabitacionesFM()
# juego.laberinto.entrar() 

# juego = Juego()
# juego.crear4Habitaciones4BestiasFM()
# sm = "pepe"
# juego.laberinto.entrar(sm)
# juego.lanzarHilos()
# time.sleep(10)
# juego.detenerHilos()