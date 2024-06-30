from ElementoMapa.Leaf.Decorator.Decorator import Decorator
from Command.Entrar import Entrar

class Bomba(Decorator):

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
    
    def agregarObservadoresActiva(self, obs):
        self.obsActiva.append(obs)

    def aceptar(self, visitor):
        print("Visitar bomba")
        visitor.visitarBomba(self)
    
    def entrar(self, e):
        if self.activa:
            print("¡Te has metido en la bomba!")
            print("¡Explotaste!")
            if e.esPersonaje() and e.defensa > 0:
                defensa_efectiva = min(e.defensa, self.damage)
                dano_recibido = self.damage - defensa_efectiva
                e.defensa -= defensa_efectiva
            else:
                dano_recibido = self.damage

            e.setCorazones(e.corazones - dano_recibido)
            self.activa = False
            
            for co in self.commands:
                if co.esEntrar():
                    self.commands.remove(co)
            for obs in self.obsActiva:
                obs.visualBomba(self)
        else:
            if self.componente is not None:
                self.componente.entrar(e)
