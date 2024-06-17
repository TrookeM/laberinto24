from Command.Usar import Usar
from Command.Coger import Coger
from Command.Soltar import Soltar

from ElementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Artefacto(ElementoMapa, ABC):
    
    def __init__(self):
        super().__init__()
        self.ref = None
        self.obsPos = []
        
    def entrar(self, obj):
        self.padre.objChildren.remove(self)
        obj.mochila.addArtefacto(self)

        for com in self.commands:
            if com.esCoger:
                self.deleteCommand(com)

        self.addCommand(Soltar())
        self.addCommand(Usar())
        for obs in self.obsPos:
            obs.visualObjeto(self)

    def soltar(self,ente):
        ente.posicion.addChild(self)
        ente.mochila.soltarArtefacto(self)
        for com in self.commands:
            if com.esSoltar():
                self.deleteCommand(com)
        for com in self.commands:
            if com.esUsar():
                self.deleteCommand(com)
        self.addCommand(Coger())
        for obs in self.obsPos:
            obs.visualObjeto(self)

    def agregarObservadorPosicion(self, observador):
        self.obsPos.append(observador)

    @abstractmethod
    def usar(self, obj):
        pass