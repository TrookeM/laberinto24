from Artefactos.Artefacto import Artefacto

class Pocion(Artefacto):
#
    def __init__(self):
        super().__init__()
        self.vida = 50

    def esPocion(self):
        return True
    
    def aceptar(self, vst):
        print("Pocion encontrada")
        vst.visitarPocion(self)

    def usar(self, o):
        o.setCorazones(o.corazones + self.vida)
        o.mochila.usado(self)

    def __str__(self):
        return "Pocion nº: " + str(self.ref)
