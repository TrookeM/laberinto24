from abc import ABC, abstractmethod

class Orientacion(ABC):

    @abstractmethod
    def getElement(self,cont):
        pass

    @abstractmethod
    def putElementOn(self,em,cont):
        pass
    
    @abstractmethod
    def aceptar(self,visitor,forma):
        pass
    
    @abstractmethod
    def verPosicion(self,forma):
        pass

    @abstractmethod
    def getCommands(self,forma,ente):
        pass

    @abstractmethod
    def moverA(self, ente):
        pass
    
    @abstractmethod
    def recorrerEn(self,cont,func):
        pass