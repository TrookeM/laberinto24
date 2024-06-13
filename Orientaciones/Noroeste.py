from Orientaciones.Orientacion import Orientacion

class Noroeste(Orientacion):
    __instance = None

    def __init__(self):
        if Noroeste.__instance is None:
            Noroeste.__instance = self
    
    def obtenerInstancia():
        if Noroeste.__instance is None:
            Noroeste.__instance = Noroeste()
        
        return Noroeste.__instance
    
    def getElement(self,cont):
        return cont.noroeste
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]-1,forma.punto[1]-1)
        forma.noroeste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("A terra dos galleguinhos.")
        forma.noroeste.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.noroeste = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.noroeste.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.noroeste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.noroeste.recorrer(func)
