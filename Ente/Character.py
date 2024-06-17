from Ente.Ente import Ente
from Cuerpo.Cuerpo import Cuerpo
class Character(Ente):
    
    def __init__(self):
        super().__init__()
        self.seudonimo=None
        self.mochila=None
        self.cuerpo=Cuerpo()

    def obtenerComandosCuerpo(self):
        return self.cuerpo.obtenerComandos(self)
    
    def obtenerBatePinchos(self):
        return self.cuerpo.obtenerArma()

    def setBatePinchos(self,obj):
        self.cuerpo.setBatePinchos(obj)

    def setPosicion(self, pos):
        self.posicion = pos
        for obs in self.obsPosition:
            obs.visualCuerpo()
    
    def setVidas(self, vida):
        self.vidas = vida
        print("Vidas de ",str(self),":",str(self.vidas))
        for obs in self.obsCorazones:
            obs.visualcorazoneshero()
    
    def fenece(self):
        self.juego.personajeMuere()

    def buscarEnemigo(self):
        return self.juego.searchAntagonist()
    
    def obtenerComandos(self, ente):
        return self.posicion.obtenerComandos(self)
    
    def esPersonaje(self):
        return True
    
    def __str__(self):
        return "Soy " + str(self.seudonimo)
    
    def __repr__(self):
        return "Soy " + str(self.seudonimo)