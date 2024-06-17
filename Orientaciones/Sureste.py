from Orientaciones.Orientacion import Orientacion

class Sureste(Orientacion):
    __instance = None

    def __init__(self):
        if Sureste.__instance is None:
            Sureste.__instance = self
    
    def obtenerInstancia(self):
        if Sureste.__instance is None:
            Sureste.__instance = Sureste()
        
        return Sureste.__instance
    
    def getElement(self,cont):
        return cont.sureste
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]+1,forma.punto[1]+1)
        forma.sureste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Sureste.")
        forma.sureste.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.sureste = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.sureste.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.sureste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.sureste.recorrer(func)
