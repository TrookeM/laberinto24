from ElementoMapa.Leaf.Decorator.Decorator import Decorator
from Command.Entrar import Entrar

class Bomba (Decorator):

    def __init__(self):
        super().__init__()
        self.num = None
        self.activa = True
        self.damage = 20
        self.obsActiva = []
        c = Entrar()
        c.receiver = self
        self.commands.append(c)

    def esBomba(self):
        return True
    
    def agregarObservadoresActiva(self,obs):
        self.obsActiva.append(obs)

    def aceptar(self,visitor):
        print("Visitar bomba")
        visitor.visitarBomba(self)
    
    def entrar(self, e):
        if self.activa:
            print("¡Te has metido en la bomba!")
            print("Explotaste carajo")
            calculo=e.corazones-self.damage
            e.setCorazones(calculo)

            self.activa=False
            
            for co in self.commands:
                if co.esEntrar():
                    self.commands.remove(co)
            for obs in self.obsActiva:
                obs.visualBomba(self)
        else:
            if self.componente is not None:
                self.componente.entrar(e)
    