from Orientaciones.Oeste import Oeste
from Orientaciones.Norte import Norte
from Orientaciones.Este import Este
from Orientaciones.Sur import Sur
from Orientaciones.Noreste import Noreste
from Orientaciones.Noroeste import Noroeste
from Orientaciones.Sureste import Sureste
from Orientaciones.Suroeste import Suroeste
from Estado.Vivo import Vivo
import sys
sys.setrecursionlimit(150000)
from abc import ABC,abstractmethod
class Ente(ABC):

    def __init__(self):
        self.corazones = 100
        self.poder = 10
        self.estado = Vivo()
        self.posicion= None
        self.juego = None
        self.obsPosition = []
        self.obsCorazones = []


    def subscribePosicion(self,obs):
        self.obsPosition.append(obs)

    def subscribeVida(self,obs):
        self.obsCorazones.append(obs)

    def setPosicion(self,pos):
        self.posicion = pos
    
    def setCorazones(self,corazones):
        self.corazones = corazones
        print(str(self), " corazones: ",str(self.corazones))

    def atacar(self):
        unEnte = self.buscarEnemigo()
        if unEnte is not None:
            unEnte.esAtacadoPor(self)
    
    def esAtacadoPor(self,unEnte):
        self.estado.enteEsAtacadoPor(self,unEnte)

    def puedeSerAtacadoPor(self,unEnte):
        print("¿Puede ser atacado?")
        self.recalcularVidas(unEnte)
        if self.verificarEstado():
            self.fenece()

    def recalcularVidas(self, ente):
        if ente.esPersonaje():
            arma = ente.obtenerBatePinchos()
        calc = (self.corazones) - (ente.poder + arma.poder)
        if calc > self.corazones:
            self.setCorazones(self.corazones)
        else:
            self.setCorazones(calc)
        if self.corazones < 0:
            self.setCorazones(0)
    
    def verificarEstado(self):
        if self.corazones == 0:
            return True
        else:
            return False
        
    @abstractmethod
    def buscarEnemigo(self):
        pass

    def estaVivo(self):
        return self.estado.estaVivo()
    
    def irA(self,unaOr):
        unaOr.moverA(self)

    def irAlNorte(self):
        self.irA(Norte.obtenerInstancia(self))

    def irAlEste(self):
        self.irA(Este.obtenerInstancia(self))

    def irAlOeste(self):
        self.irA(Oeste.obtenerInstancia(self))

    def irAlSur(self):
        self.irA(Sur.obtenerInstancia(self))

    def irAlNoreste(self):
        self.irA(Noreste.obtenerInstancia(self))

    def irAlNoroeste(self):
        self.irA(Noroeste.obtenerInstancia(self))

    def irAlSureste(self):
        self.irA(Sureste.obtenerInstancia(self))

    def irAlSuroeste(self):
        self.irA(Suroeste.obtenerInstancia(self))

    def esPersonaje(self):
        return False
    
    def esBicho(self):
        return False
    
    @abstractmethod
    def fenece(self):
        pass