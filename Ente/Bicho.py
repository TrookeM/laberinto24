from Ente.Ente import Ente
from Estado.Muerto import Muerto
from Modo.Agresivo import Agresivo
import random
import sys
sys.setrecursionlimit(150000)

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo = None
        self.numero_identificador = None
        self.curado = False  # Atributo para controlar si ya se ha curado

    def set_posicion(self, pos):
        self.posicion = pos
        for observador in self.obsPosition:
            observador.visualBicho(self)

    def set_corazones(self, corazones):
        self.corazones = corazones
        print("Corazones de ", str(self), ":", str(self.corazones))
        for observador in self.obsCorazones:
            observador.corazonesBicho(self)

    def buscarEnemigo(self):
        return self.juego.visualBicho(self)

    def actuar(self):
        while self.estaVivo():
            self.estado.actua(self)

    def obtener_orientacion_aleatoria(self):
        return self.posicion.getRandOri()
    
    def puedeActuar(self):
        self.modo.actua(self)

    def ente_muere(self):
        self.muerto()

    def muerto(self):
        self.estado = Muerto()
        self.muere()
        self.juego.muere_bicho()

    def muere(self):
        print(str(self), " ha muerto.")
        self.corazones = 0
        self.estado = Muerto()

    def cambiar(self):
        entity = self.juego.buscar_bicho(self)
        if entity is not None:
            numero_aleatorio = random.randint(1, 10)

            if numero_aleatorio > 9:
                self.modo = Agresivo()
            
                for observador in self.obsPosition:
                    observador.visualBicho(self)

    def es_bicho(self):
        return True
    
    def __str__(self):
        return "Bicho" + " id: " + str(self.numero_identificador) + " " + str(self.modo)
    
    def __repr__(self):
        return "Bicho" + str(self.modo) + str(self.numero_identificador)

    def esAtacadoPor(self, unEnte):
        self.estado.enteEsAtacadoPor(self, unEnte)
        # Aquí agregamos la llamada a curar si el modo es curativo y aún no se ha curado
        if self.modo.esCurativo() and not self.curado:
            self.modo.curar(self)
            self.curado = True  # Marcamos que ya se ha curado una vez
