from Orientaciones.Orientacion import Orientacion

class Noreste(Orientacion):
    __instance = None

    def __init__(self):
        if Noreste.__instance is None:
            Noreste.__instance = self
    
    def obtenerInstancia():
        if Noreste.__instance is None:
            Noreste.__instance = Noreste()
        
        return Noreste.__instance
    
    def getElement(self,cont):
        return cont.noreste
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]+1,forma.punto[1]-1)
        forma.noreste.verPosicion(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Donde abunda la degeneración y el separatismo.")
        forma.noreste.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.noreste = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.noreste.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.noreste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.noreste.recorrer(func)
