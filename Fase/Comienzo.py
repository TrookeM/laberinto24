
from Fase.Fase import Fase
from Fase.Jugando import Jugando

class Comienzo(Fase):
    
    def addCharacter(self, ch, game):
        game.puedeAgregarPersonaje(ch)

    def lanzarBichos(self,juego):
        juego.puedeLanzarBichos()
        juego.fase = Jugando()

    def esInicio(self):
        return True
