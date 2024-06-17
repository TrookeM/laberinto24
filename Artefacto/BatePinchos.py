from Artefacto.Artefacto import Artefacto
from Command.Usar import Usar
from Command.Soltar import Soltar


class BatePinchos(Artefacto):

    def __init__(self):
        super().__init__()
        self.poder = 25

    def esBatePinchos(self):
        return True

    def aceptar(self, vst):
        print("Visitar BatePinchos")
        vst.visitarBatePinchos(self)
    
    def usar(self, o):
        o.setBatePinchos(self)
        o.mochila.usado(self)

        for c in self.commands:
            if c.esSoltar():
                self.deleteCommand(c)
        for c in self.commands:
            if c.esUsar():
                self.deleteCommand(c)
    
    def desequipar(self,ente):
        ente.setBatePinchos(None)
        ente.mochila.addArtefacto(self)
        
        firstAction = Usar()
        firstAction.receiver= self

        secondAction = Soltar()
        secondAction.receiver = self

        self.addCommand(firstAction)
        self.addCommand(secondAction)

    def __str__(self):
        return "BatePinchos REF nº: " +str(self.ref)