from Artefactos.Artefacto import Artefacto

class Pan(Artefacto):
#
    def __init__(self):
        super().__init__()
        self.vida = 10

    def esPan(self):
        return True
    
    def aceptar(self, vst):
        print("Pan encontrado")
        vst.visitarPan(self)

    def usar(self, o):
        o.setCorazones(o.corazones + self.vida)
        o.mochila.usado(self)

    def __str__(self):
        return "Pan nº: " + str(self.ref)
