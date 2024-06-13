from Juego.Juego import Juego
from ElementoMapa.Container.HabitacionFuego import HabitacionFuego
from ElementoMapa.ParedFuego import ParedFuego

class JuegoFuego(Juego):

    def fabricarHabitacion(self, id):
        return HabitacionFuego(id)

    def fabricarPared(self):
        return ParedFuego()
    
juego = JuegoFuego()
juego.laberinto2HabFM()

hab = juego.laberinto.getHab(1)
print(juego.laberinto)
print(hab.entrar())
print(hab.entrar())
print(hab.norte.entrar())
print(hab.norte.entrar())