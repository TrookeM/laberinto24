from Orientaciones.Orientacion import Orientacion

class Suroeste(Orientacion):
    __instance = None

    def __init__(self):
        if Suroeste.__instance is None:
            Suroeste.__instance = self
    
    def obtenerInstancia(self):
        if Suroeste.__instance is None:
            Suroeste.__instance = Suroeste()
        
        return Suroeste.__instance
    
    def getElement(self,cont):
        return cont.suroeste
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]-1,forma.punto[1]+1)
        forma.suroeste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("We wuz kangz.")
        forma.suroeste.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.suroeste = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.suroeste.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.suroeste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.suroeste.recorrer(func)
