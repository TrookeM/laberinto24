from Orientaciones.Orientacion import Orientacion

class Este(Orientacion):
    __instance = None

    def __init__(self):
        if Este.__instance is None:
            Este.__instance = self
    
    def obtenerInstancia():
        if Este.__instance is None:
            Este.__instance = Este()
        
        return Este.__instance
    
    def getElement(self,cont):
        return cont.este
    
    def verPosicion(self,forma):
        unPunto = (forma.punto[0]+1,forma.punto[1])
        forma.este.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Bienvenido a la Terreta.")
        forma.este.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.este = em
    
    def moverA(self,ente):
        cont = ente.posicion.form
        cont.este.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.este.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.este.recorrer(func)
