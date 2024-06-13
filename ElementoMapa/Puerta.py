from ElementoMapa.ElementoMapa import ElementoMapa
from Command.Abrir import Abrir
from Command.Entrar import Entrar
from Command.Cerrar import Cerrar
from Estado.EstadoPuerta.Cerrada import Cerrada
from Estado.EstadoPuerta.Abierta import Abierta

class Puerta(ElementoMapa):

    def __init__(self): 
        super().__init__()
        self.estado = Cerrada()
        self.lado1 = None
        self.lado2 = None
        self.visited = False
        self.observers = []

    def entrar(self,ente):
        if self.estaAbierta():
            if ente.posicion == self.lado1:
                self.lado2.entrar(ente)
            else:
                self.lado1.entrar(ente)
        else:
            print(str(ente)," se chocó con una puerta.")

    def subsOpened(self,observer):

        self.observers.append(observer)

    def EstimarDistancia(self, obj, coord):
        
        if self.visited:
            return self
        
        self.visited=True
        
        if obj.ref == self.lado1.ref:
        
            self.lado2.getPunto(coord)
            self.lado2.estimarPosicion()
        
        else:
            self.lado1.getPunto(coord)
            self.lado1.estimarPosicion()

    def aceptar(self,visitor):
        print("Visitando una puerta")
        visitor.visitarPuerta(self)

    def abrir(self, ente = None):

        self.estado.abrir(self)

    def puedeAbrirse(self, ente=None):
        self.estado = Abierta()
        self.deleteAbrir()

        com1 = Entrar()
        com2 = Cerrar()
        
        com1.receiver = self
        com2.receiver = self

        self.addCommand(com1)
        self.addCommand(com2)

        self.lado1.notifySubs()
        self.lado2.notifySubs()
        self.notificarSubs()

    def notificarSubs(self):
        for obs in self.observers:
            obs.mostrar(self)

    def deleteAbrir(self):
        for com in self.commands:
            if com.esAbrir():
                self.deleteCommand(com)
                return

    def cerrar(self):
        self.estado = Cerrada()
        self.deleteClose()
        self.deleteEntrar()

        com = Abrir()

        com.receiver = self

        self.addCommand(com)

        self.lado1.notifySubs()
        self.lado2.notifySubs()
        self.notificarSubs()

    def deleteClose(self):
        for com in self.commands:
            if com.esCerrar():
                self.deleteCommand(com)
                return
    
    def deleteEntrar(self):
        for com in self.commands:
            if com.esEntrar():
                self.deleteCommand(com)
                return
        
    def esPuerta(self):
        return True
    
    def estaAbierta(self):
        return self.estado.estaAbierta()
