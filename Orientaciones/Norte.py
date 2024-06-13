from Orientaciones.Orientacion import Orientacion

class Norte(Orientacion):
    __instance = None

    def __init__(self):
        if Norte.__instance is None:
            Norte.__instance = self
    
    def obtenerInstancia():
        if Norte.__instance is None:
            Norte.__instance = Norte()
        
        return Norte.__instance
    
    def getElement(self,cont):
        return cont.norte
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0],forma.punto[1]-1)
        forma.norte.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Acabas de entrar en la TIERRA DE LOS VALIENTES.")
        forma.norte.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.norte = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.norte.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.norte.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.norte.recorrer(func)
