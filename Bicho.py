import time
import random

class Criatura:
    def __init__(self):
        self.posicion = None
        self.juego = None
        self.vida = None
        self.poder = None
    
    def irNorte(self):
        self.posicion.irNorte(self)
    def irEste(self):
        self.posicion.irEste(self)
    def irSur(self):
        self.posicion.irSur(self)
    def irOeste(self):
        self.posicion.irOeste(self)
    def atacar(self):
        enemigo = self.encontrarEnemigo()
        if enemigo:
            enemigo.esAtacadoPor(self)
    def encontrarEnemigo(self):
        pass
    def esAtacadoPor(self, otro):
        pass

class Persona(Criatura):
    def __init__(self, nombre):
        super().__init__()
        self.vida = 20
        self.poder = 1
        self.nombre = nombre
    def __str__(self):
        return self.nombre
    def encontrarEnemigo(self):
        return self.juego.encontrarBestia(self.posicion)
    def esAtacadoPor(self, otro):
        self.vida -= otro.poder
        print(self, "es atacado por", otro)
        if self.vida <= 0:
            print(self, "ha muerto, FIN DEL JUEGO")
            self.juego.detenerHilos()
        else:
            print("La vida de", self, "ahora es", self.vida)

class Bestia(Criatura):
    def __init__(self, modo):
        super().__init__()
        self.modo = modo
        self.poder = 2
        self.vida = 10
        self.num = 0
    
    def __str__(self):
        template = 'Bestia-{0.modo}{0.num}'
        return template.format(self)
    
    def esAgresiva(self):
        return self.modo.esAgresiva()

    def esPerezosa(self):
        return self.modo.esPerezosa()
    
    def actuar(self):
        self.modo.actuar(self)
    
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    def iniciar(self):
        self.actuar()

    def detener(self):
        print(self , " ha sido detenida")
        exit(0)

    def encontrarEnemigo(self):
        return self.juego.encontrarPersona(self.posicion)

class Modo:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def esAgresiva(self):
        return False
    def esPerezosa(self):
        return False
    def actuar(self, bestia):
        while bestia.vida > 0:
            self.dormir(bestia)
            self.caminar(bestia)
            self.atacar(bestia)
    def caminar(self, bestia):
        bestia.caminarAleatorio()
    def dormir(self, bestia):
        print(bestia, " está durmiendo")
        time.sleep(3)
    def atacar(self, bestia):
        bestia.atacar()

class Agresiva(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Agresiva"
    
    def esAgresiva(self):
        return True

    def imprimir(self):
        print("Bestia Agresiva")

class Perezosa(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Perezosa"
    
    def imprimir(self):
        print("Bestia Perezosa")

    def esPerezosa(self):
        return True