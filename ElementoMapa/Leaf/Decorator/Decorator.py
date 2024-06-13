from ElementoMapa.Leaf.Leaf import Leaf

class Decorator (Leaf):

    def __init__(self):
        super().__init__()
        self.componente = None

    def recorrer(self, o):
        o(self)
        if self.componente is not None:
            self.componente.recorrer(o)