from ElementoMapa.Leaf.Leaf import Leaf

class Tunel(Leaf):
    
    def __init__(self):
        super().__init__()
        self.laberinto = None

    def entrar(self, e):
        if self.laberinto is None:
            self.laberinto = e.juego.clonarLaberinto()
            hab = self.laberinto.getHab(self.padre.ref)
            for hijo in hab.objChildren:
                if hijo.esTunel():
                    hijo.laberinto = self.padre
        self.laberinto.entrar(e)

    def aceptar(self, visitor):
        print("Visitar tunel")
        visitor.visitarTunel(self)

    def esTunel(self):
        return True
    
    def __str__(self):
        return "¡Túnel!"
    
    def __repr__(self):
        return "¡Túnel!"