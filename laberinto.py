import random

class ElementoMapa:
    def __init__(self):
        pass
    
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

    def recorrer(self,unBloque):
        unBloque(self)

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.num = None    
        self.forma = None    

    def agregarHijo(self, componente):
        self.hijos.append(componente)

    def removerHijo(self, componente):
        self.hijos.remove(componente)
    
    def imprimir(self):
        print("Contenedor")
    
    def caminarAleatorio(self, alguien):
        pass

    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)
    
    def removerOrientacion(self, orientacion):
        self.forma.removerOrientacion(orientacion)

    def caminarAleatorio(self, alguien):        
        orientacion = self.forma.getOrientacionAleatoria()
        orientacion.caminarAleatorio(alguien)
   
    def irNorte(self, alguien):
        self.forma.irNorte(alguien)

    def irEste(self, alguien):
        self.forma.irEste(alguien)

    def irSur(self, alguien):
        self.forma.irSur(alguien)

    def irOeste(self, alguien):
        self.forma.irOeste(alguien)

    def setEMinOr(self, em, orientacion):
        self.forma.setEMinOr(em, orientacion)
    
    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        self.forma.recorrer(unBloque)

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.agregarHijo(habitacion)

    def entrar(self, alguien):
        self.hijos[0].entrar(alguien)

    def imprimir(self):
        print("Laberinto")   
    
    def obtenerHabitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None

    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
    
    def getOrientations(self):
        pass

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(str(alguien) + " entra a la habitación " + str(self.num) + "\n")
        alguien.posicion = self
    
    def imprimir(self):
        print("Habitación")

    def esHabitacion(self):
        return True

    def __str__(self):
        return "Habitación-" + str(self.num) + "\n"
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("Hoja")

class Decorador(Hoja):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def imprimir(self):
        print("Decorador")

class Tunel(Leaf):
    def __init__(self):
        super().__init__()
        self.maze = None
    def enter(self,alguien):
        print(str(alguien) + " entrar al tunel"+"\n")
        self.maze=alguien.game.cloneMaze()
        self.maze.enter(alguien)

class Bomba(Decorador):
    def __init__(self):
        super().__init__()
        self.activa = False

    def imprimir(self):
        print("Bomba")

    def entrar(self, alguien):
        print(alguien + " ha caído en una bomba" + "\n")

class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def imprimir(self):
        print("Pared")

    def entrar(self, alguien):
        print(alguien , " se ha encontrado con una pared" + "\n")

class ParedConBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
    
    def imprimir(self):
        print("ParedConBomba")

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    
    def entrar(self, alguien):
        if self.abierta:
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
            print("La puerta " + str(self) + " está cerrada" + "\n")
    
    def __str__(self):
        return "Puerta-" + str(self.lado1) + "-" + str(self.lado2)
    
    def abrir(self):
        print("Abriendo la puerta entre " + str(self.lado1) + " y " + str(self.lado2) + "\n")
        self.abierta = True
    
    def cerrar(self):
        print("Cerrando la puerta entre " + str(self.lado1) + " y " + str(self.lado2) + "\n")

    def esPuerta(self):
        return True

class Orientacion:
    def __init__(self):
        pass
    
    def caminarAleatorio(self, alguien):
        pass
    
    def setEMinOr(self, em, unContenedor):
        pass

    def recorrerEn(self, unBloque, unContenedor):
        pass

class Norte(Orientacion):
    _instancia = None

    def __init__(self):
        if not Norte._instancia:
            super().__init__()
            Norte._instancia = self

    def setEMinOr(self, em, unContenedor):
        unContenedor.norte = em

    @classmethod
    def obtener_instancia(cls):
        if not cls._instancia:
            cls._instancia = Norte()
        return cls._instancia

    def imprimir(self):
        print("Norte")
    
    def caminarAleatorio(self, alguien):
        alguien.irNorte()

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.norte.recorrer(unBloque)

class Sur(Orientacion):
    _instancia = None

    def __init__(self):
        if not Sur._instancia:
            super().__init__()  
            Sur._instancia = self

    @staticmethod 
    def obtener_instancia():
        if not Sur._instancia:
            Sur()
        return Sur._instancia
    
    def imprimir(self):
        print("Sur")
    
    def caminarAleatorio(self, alguien):
        alguien.irSur()
    
    def setEMinOr(self, em, unContenedor):
        unContenedor.sur = em
    
    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.sur.recorrer(unBloque)

class Este(Orientacion):
    _instancia = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')
        #if not Este._instancia:
        #    super().__init__()
        #   Este._instancia = self

    @classmethod
    def obtener_instancia(cls):
        if cls._instancia is None:
            print('Creando nueva instancia')
            cls._instancia = cls.__new__(cls)
        return cls._instancia
    
    def caminarAleatorio(self, alguien):
        alguien.irEste()
    
    def setEMinOr(self, em, unContenedor):
        unContenedor.este = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.este.recorrer(unBloque)
        
class Oeste(Orientacion):
    _instancia = None

    def __init__(self):
        if not Oeste._instancia:
            super().__init__()
            Oeste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Oeste._instancia:
            Oeste()
        return Oeste._instancia
    
    def imprimir(self):
        print("Oeste")
    
    def caminarAleatorio(self, alguien):
        alguien.irOeste()

    def setEMinOr(self, em, unContenedor):
        unContenedor.oeste = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.oeste.recorrer(unBloque)

class Noreste(Orientacion):
    _instancia = None
    
    def __init__(self):
        if not Noreste._instancia:
            super().__init__()
            Noreste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Noreste._instancia:
            Noreste()
        return Noreste._instancia

    def imprimir(self):
        print("Noreste")

    def caminarAleatoriamente(self, alguien):
        alguien.irNoreste()

    def establecerEntidadMinOr(self, em, unContenedor):
        unContenedor.noreste = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.noreste.recorrer(unBloque)
        
class Noroeste(Orientacion):
    _instancia = None
    
    def __init__(self):
        if not Noroeste._instancia:
            super().__init__()
            Noroeste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Noroeste._instancia:
            Noroeste()
        return Noroeste._instancia

    def imprimir(self):
        print("Noroeste")

    def caminarAleatoriamente(self, alguien):
        alguien.irNoroeste()

    def establecerEntidadMinOr(self, em, unContenedor):
        unContenedor.noroeste = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.noroeste.recorrer(unBloque)
        
class Sureste(Orientacion):
    _instancia = None
    
    def __init__(self):
        if not Sureste._instancia:
            super().__init__()
            Sureste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Sureste._instancia:
            Sureste()
        return Sureste._instancia

    def imprimir(self):
        print("Sureste")

    def caminarAleatoriamente(self, alguien):
        alguien.irSureste()

    def establecerEntidadMinOr(self, em, unContenedor):
        unContenedor.sureste = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.sureste.recorrer(unBloque)
        
class Suroeste(Orientacion):
    _instancia = None
    
    def __init__(self):
        if not Suroeste._instancia:
            super().__init__()
            Suroeste._instancia = self

    @staticmethod
    def obtener_instancia():
        if not Suroeste._instancia:
            Suroeste()
        return Suroeste._instancia

    def imprimir(self):
        print("Suroeste")

    def caminarAleatoriamente(self, alguien):
        alguien.irSuroeste()

    def establecerEntidadMinOr(self, em, unContenedor):
        unContenedor.suroeste = em

    def recorrerEn(self, unBloque, unContenedor):
        unContenedor.suroeste.recorrer(unBloque)


class Forma:
    def __init__(self):
        self.orientaciones = []

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)   

    def removerOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def getOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def setEMinOr(self, em, orientacion):
        orientacion.setEMinOr(em, self)

    def recorrer(self,unBloque):
        for orientacion in self.orientaciones:
            orientacion.recorrerEn(unBloque,self)

class Rectangulo(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.agregarTodasLasOrientaciones()

    def agregarTodasLasOrientaciones(self):
        self.agregarOrientación(Norte.obtener_instancia())
        self.agregarOrientación(Sur.obtener_instancia())
        self.agregarOrientación(Este.obtener_instancia())
        self.agregarOrientación(Oeste.obtener_instancia())

    def irNorte(self, alguien):
        self.norte.entrar(alguien)

    def irEste(self, alguien):
        self.este.entrar(alguien)

    def irSur(self, alguien):
        self.sur.entrar(alguien)

    def irOeste(self, alguien):
        self.oeste.entrar(alguien)

class Hexagono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.noreste = None
        self.sureste = None
        self.sur = None
        self.suroeste = None
        self.noroeste = None
        self.agregarTodasLasOrientaciones()

    def agregarTodasLasOrientaciones(self):
        self.agregarOrientación(Norte.obtener_instancia())
        self.agregarOrientación(Noreste.obtener_instancia())
        self.agregarOrientación(Sureste.obtener_instancia())
        self.agregarOrientación(Sur.obtener_instancia())
        self.agregarOrientación(Suroeste.obtener_instancia())
        self.agregarOrientación(Noroeste.obtener_instancia())

    def irNorte(self, alguien):
        self.norte.entrar(alguien)

    def irNoreste(self, alguien):
        self.noreste.entrar(alguien)

    def irSureste(self, alguien):
        self.sureste.entrar(alguien)

    def irSur(self, alguien):
        self.sur.entrar(alguien)

    def irSuroeste(self, alguien):
        self.suroeste.entrar(alguien)

    def irNoroeste(self, alguien):
        self.noroeste.entrar(alguien)

