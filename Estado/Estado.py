from abc import ABC
import sys
sys.setrecursionlimit(150000)
class Estado(ABC):
    
    def actua(unBicho):
        pass
    
    def esAtacadoPor(self,atacado,atacante):
        pass
    
    def estaVivo(self):
        pass

    def esVivo(self):
        return False
    
    def esMuerto(self):
        return False
    
    def esAbierta(self):
        return False
    
    def esCerrada(self):
        return False