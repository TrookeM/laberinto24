from Estado.Estado import Estado

class Cerrada(Estado):
    
    def abrir(self,gate):
        gate.puedeAbrirse()

    def estaAbierta(self):
        return False
    
    def esCerrada(self):
        return True
    
    def __str__(self):
        return "Cerrada"
    
    def __repr__(self):
        return "Cerrada"