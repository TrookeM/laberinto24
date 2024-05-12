import random

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Comando:
    def __init__(self, receptor):
        self.receptor = receptor
    
    def ejecutar(self):
        pass
    
    def esEntrar(self):
        return False

class Abrir(Comando):
    def ejecutar(self):
        self.receptor.eliminarComando(self)
        self.receptor.agregarComando(Cerrar(self.receptor))
        self.receptor.agregarComando(Entrar(self.receptor))
        self.receptor.abrir()

class Cerrar(Comando):
    def ejecutar(self):
        self.receptor.eliminarComando(self)
        self.receptor.agregarComando(Abrir(self.receptor))
        self.receptor.cerrar()

class Entrar(Comando):
    def ejecutar(self):
        self.receptor.entrar()
    
    def esEntrar(self):
        return True

class ElementoMapa:
    def __init__(self):
        self.comandos = []
    
    def entrar(self, alguien):
        pass

    def imprimir(self):
        print("ElementoMapa")
    
    def esHabitacion(self):
        return False

    def esPuerta(self):
        return False
    
    def recorrer(self, unBloque):
        pass
    
    def abrir(self):
        pass
    
    def cerrar(self):
        pass
    
    def recorrer(self, unBloque):
        unBloque(self)
        
    def agregarComando(self, comando):
        self.comandos.append(comando)
    
    def eliminarComando(self, comando):
        self.comandos.remove(comando)
    
    def obtenerComandos(self):
        return self.comandos
    
    def aceptar(self, visitante):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.numero = None    
        self.forma = None    
    
    def obtenerPunto(self):
        return self.forma.obtenerPunto()

    def establecerPunto(self, punto):
        self.forma.establecerPunto(punto)
    
    def obtenerExtension(self):
        return self.forma.extension
    
    def establecerExtension(self, extension):
        self.forma.extension = extension
    
    def agregarHijo(self, componente):
        self.hijos.append(componente)

    def eliminarHijo(self, componente):
        self.hijos.remove(componente)
    
    def imprimir(self):
        print("Contenedor")
    
    def caminarAleatoriamente(self, alguien):
        pass
    
    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)
    
    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)
    
    def obtenerOrientaciones(self):
        return self.forma.orientaciones

    def caminarAleatoriamente(self, alguien):        
        orientacion = self.forma.obtenerOrientacionAleatoria()
        orientacion.caminarAleatoriamente(alguien)
   
    def irNorte(self, alguien):
        self.forma.irNorte(alguien)
    
    def irEste(self, alguien):
        self.forma.irEste(alguien)
    
    def irSur(self, alguien):
        self.forma.irSur(alguien)
    
    def irOeste(self, alguien):
        self.forma.irOeste(alguien)
    
    def establecerEMinOr(self, em, orientacion):
        self.forma.establecerEMinOr(em, orientacion)
    
    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        self.forma.recorrer(unBloque)
    
    def obtenerComandos(self):
        lista = []
        lista += self.comandos
        for hijo in self.hijos:
            lista += hijo.obtenerComandos()
        lista += self.forma.obtenerComandos()
        return lista

    def calcularPosicion(self):
        self.forma.calcularPosicion()  
    
class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.agregarHijo(habitacion)

    def entrar(self, alguien):
        self.hijos[0].entrar(alguien)

    def imprimir(self):
        print("Laberinto")   
    
    def obtenerHabitacion(self, numero):
        for habitacion in self.hijos:
            if habitacion.numero == numero:
                return habitacion
        return None
    
    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)        

    def obtenerOrientaciones(self):
        pass
    
    def aceptar(self, visitante):
        for hijo in self.hijos:
            hijo.aceptar(visitante)   

class Habitacion(Contenedor):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero

    def entrar(self, alguien):
        print(str(alguien) + " entra a la habitación " + str(self.numero))
        alguien.posicion = self
    
    def imprimir(self):
        print("Habitación")

    def esHabitacion(self):
        return True

    def __str__(self):
        return "Habitación-" + str(self.numero)    

    def aceptar(self, visitante):
        visitante.visitarHabitacion(self)
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("Hoja")

class Tunel(Hoja):
    def __init__(self):
        super().__init__()
        self.laberinto = None
    
    def entrar(self, alguien):
        print(str(alguien) + " entra al túnel" + "\n")
        self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrar(alguien)

class Decorador(Hoja):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def imprimir(self):
        print("Decorador")

class Bomba(Decorador):
    def __init__(self):
        super().__init__()
        self.activa = False

    def imprimir(self):
        print("Bomba")

    def entrar(self, alguien):
        print(alguien + " caminó hacia una bomba" + "\n")

class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def imprimir(self):
        print("Pared")

    def entrar(self, alguien):
        print(alguien , " se encontró con una pared")

    def calcularPosicionDesde(self, unaForma, unPunto):
        pass
