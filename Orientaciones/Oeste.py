from Orientaciones.Orientacion import Orientacion

class Oeste(Orientacion):
    __instance = None

    def __init__(self):
        if Oeste.__instance is None:
            Oeste.__instance = self
    
    def obtenerInstancia():
        if Oeste.__instance is None:
            Oeste.__instance = Oeste()
        
        return Oeste.__instance
    
    def getElement(self,cont):
        return cont.oeste
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]-1,forma.punto[1])
        forma.oeste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Has puesto un pie en la Vía de la Plata.")
        forma.oeste.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.oeste = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.oeste.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.oeste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.oeste.recorrer(func)
