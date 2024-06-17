import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ElementoMapa')))

from ElementoMapa.Container.Container import Container
class Laberinto(Container):

    def __init__(self):
        super().__init__(0)


    def agregarHabitacion(self, hab):
        self.objChildren.append(hab)

    def entrar(self, ente):
        h = self.getHab(1)
        h.entrar(ente)

    def getHab(self, index):
        return self.objChildren[index - 1]
    
    def recorrer(self, order):
        for ch in self.objChildren:
            ch.recorrer(order)

    def aceptar(self, visitor):
        print("Recorrer laberinto.")
        for ch in self.objChildren:
            ch.aceptar(visitor)

    
    def __str__(self):
        detalle = "Estado del laberinto:\n _________________________ \n"

        hijos = self.objChildren
        
        for h in hijos:
            detalle = detalle + str(h) + "\n ***************"
    
        return detalle

