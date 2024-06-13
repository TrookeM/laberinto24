from Juego.Juego import Juego
from ElementoMapa.Container.HabitacionBomba import HabitacionBomba
from ElementoMapa.ParedBomba import ParedBomba

class JuegoBombas(Juego):

    def fabricarHabitacion(self, id):
        return HabitacionBomba(id)

    def fabricarPared(self):
        return ParedBomba()
    
juego = JuegoBombas()
juego.laberinto2HabFM()

hab = juego.laberinto.getHab(1)
print(juego.laberinto)
print(hab.entrar())
print(hab.entrar())
print(hab.norte.entrar())
print(hab.norte.entrar())