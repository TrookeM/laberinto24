from ElementoMapa.Leaf.Decorator.Decorator import Decorator
from Command.Entrar import Entrar
from Command.Apagar import Apagar

class Fuego(Decorator):

    def __init__(self):
        super().__init__()
        self.activo = True
        self.damage = 15
        self.obsActivo = []
        c = Entrar()
        c.receiver = self
        self.commands.append(c)
        a = Apagar(self)
        self.commands.append(a)

    def esFuego(self):
        return True

    def agregarObservadoresActivo(self, obs):
        self.obsActivo.append(obs)

    def aceptar(self, visitor):
        print("Visitar fuego")
        visitor.visitarFuego(self)

    def entrar(self, e):
        if self.activo:
            print("¡Cuidado! ¡Estás en llamas!")
            calculo = e.corazones - self.damage
            e.setCorazones(calculo)

            self.activo = False

            for co in self.commands:
                if co.esEntrar():
                    self.commands.remove(co)
            for obs in self.obsActivo:
                obs.visualFuego(self)
        else:
            if self.componente is not None:
                self.componente.entrar(e)
    
    def apagarFuego(self):
        if self.activo:
            self.activo = False
            print("El fuego ha sido apagado.")
            for obs in self.obsActivo:
                obs.visualFuego(self)
        else:
            print("El fuego ya está apagado.")