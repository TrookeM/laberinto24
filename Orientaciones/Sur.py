from Orientaciones.Orientacion import Orientacion

class Sur(Orientacion):
    __instance = None

    def __init__(self):
        if Sur.__instance is None:
            Sur.__instance = self
    
    def obtenerInstancia():
        if Sur.__instance is None:
            Sur.__instance = Sur()
        
        return Sur.__instance
    
    def getElement(self,cont):
        return cont.sur
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0],forma.punto[1]+1)
        forma.sur.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Has puesto un pie en el territorio Tartessos.")
        forma.sur.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.sur = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.sur.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.sur.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.sur.recorrer(func)
