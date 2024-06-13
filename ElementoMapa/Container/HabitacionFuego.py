from ElementoMapa.Container.Habitacion import Habitacion
from ElementoMapa.ParedFuego import ParedFuego

class HabitacionFuego(Habitacion):
    def __init__(self):
        super().__init__()
        self.pared = ParedFuego()

    def obtenerComandos(self, ente):
        return self.pared.obtenerComandos(ente)

    def aceptar(self, visitor):
        visitor.visitar(self)

    def __str__(self):
        return "Habitación de Fuego"
