from Artefacto.BatePinchos import BatePinchos
from Artefacto.Pan import Pan
from Artefacto.Pocion import Pocion
from Command.Abrir import Abrir
from Command.Coger import Coger
from ElementoMapa.Container.Armario import Armario
from ElementoMapa.Container.Habitacion import Habitacion
from ElementoMapa.Container.Laberinto import Laberinto
from ElementoMapa.Leaf.Decorator.Bomba import Bomba
from ElementoMapa.Leaf.Decorator.Fuego import Fuego
from ElementoMapa.Leaf.Tunel import Tunel
from ElementoMapa.Pared import Pared
from ElementoMapa.Puerta import Puerta
from Ente.Bicho import Bicho
from Forma.Square import Square
from Juego.Juego import Juego
from Modo.Agresivo import Agresivo
from Modo.Perezoso import Perezoso
from Orientaciones.Este import Este
from Orientaciones.Norte import Norte
from Orientaciones.Oeste import Oeste
from Orientaciones.Sur import Sur


class LaberintoBuilder():
    
    def __init__(self):
        self.juego = None
        self.maze = None
        self.dict = None

    def obtenerJuego(self):
        return self.juego
    
    def makeJuego(self):
        juego = Juego()
        juego.prototype = self.laberinto
        juego.laberinto = juego.clonarLaberinto()
        self.juego = juego

        return juego
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
    
    def fabricarModoAgresivo(self):
        return Agresivo()
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBicho(self):
        return Bicho()
    
    def fabricarPan(self,num):
        comida = Pan()
        comida.ref = num

        cmd = self.fabricarCoger()
        cmd.receiver= comida

        comida.addCommand(cmd)
        return comida
    
    def fabricarPocion(self,num):
        comida = Pocion()
        comida.ref = num

        cmd = self.fabricarCoger()
        cmd.receiver= comida

        comida.addCommand(cmd)
        return comida
    
    def fabricarForma(self):
        return Square()
    
    def fabricarArmario(self, id):
        return Armario(id)
    
    def fabricarTunel(self):
        return Tunel()
    
    def fabricarTunelEn(self, parent):

        tunel = self.fabricarTunel()
        parent.addChild(tunel)

    def fabricarArmarioEn(self, obj, num):
        armario = self.fabricarArmario(num)
        
        parent = self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver= parent

        parent.addCommand(cmd)


        parent.lado1=self
        parent.lado2=obj

        armario.form = self.fabricarForma()
        parent.lado1 = armario
        parent.lado2 = obj

        armario.addOr(self.fabricarNorte())
        armario.addOr(self.fabricarEste())
        armario.addOr(self.fabricarOeste())
        armario.addOr(self.fabricarSur())

        armario.putElementOn(self.fabricarNorte(),self.fabricarPared())
        armario.putElementOn(self.fabricarEste(),self.fabricarPared())
        armario.putElementOn(self.fabricarOeste(),self.fabricarPared())
        armario.putElementOn(self.fabricarSur(), parent)

        obj.addChild(armario)
        return armario

    def fabricarBombaEn(self,padre,num):
        bomba = self.fabricarBomba()
        bomba.num = num
        padre.addChild(bomba)

    def fabricarFuegoEn(self,padre,num):
        fuego = self.fabricarFuego()
        fuego.num = num
        padre.addChild(fuego)
    
    def fabricarBatePinchosEn(self,padre,num):
        arma = self.fabricarBatePinchos()
        arma.ref = num
        padre.addChild(arma)
        cmd = Coger()
        arma.addCommand(cmd)
        
        return arma
    
    def fabricarBichoAgresivo(self, posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoAgresivo()

        bicho.corazones = 100
        bicho.poder = 50

        return bicho
    
    def fabricarBichoPerezoso(self, posicion):
        bicho = self.fabricarBicho()
        bicho.posicion = posicion
        bicho.modo = self.fabricarModoPerezoso()

        bicho.corazones = 50
        bicho.poder = 25

        return bicho

    def fabricarBichoAlternativo(self, modo, posicion):
        hab = self.juego.getHab(posicion)

        if modo == "agresivo":
            bicho = self.fabricarBichoAgresivo(hab)
        if modo == "perezoso":
            bicho = self.fabricarBichoPerezoso(hab)
        
        if bicho is not None:
            self.juego.agregarBicho(bicho)
    
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarAbrir(self):
        return Abrir()

    def fabricarCoger(self):
        return Coger()
    
    def fabricarHabitacion(self,num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref = num
        hab.form = forma

        hab.putElementOn(self.fabricarNorte(),self.fabricarPared())
        hab.putElementOn(self.fabricarEste(),self.fabricarPared())
        hab.putElementOn(self.fabricarOeste(),self.fabricarPared())
        hab.putElementOn(self.fabricarSur(),self.fabricarPared())

        hab.addOr(self.fabricarNorte())
        hab.addOr(self.fabricarEste())
        hab.addOr(self.fabricarOeste())
        hab.addOr(self.fabricarSur())

        self.laberinto.agregarHabitacion(hab)

        return hab

    def fabricarPuertaL(self, num1, ori1, num2, ori2):
        l1 =self.laberinto.getHab(num1)
        l2 =self.laberinto.getHab(num2)

        ori1x = getattr(self,'fabricar'+ ori1)()
        ori2x = getattr(self,'fabricar'+ ori2)()

        door = self.fabricarPuerta()

        door.lado1 = l1 
        door.lado2 = l2

        com = self.fabricarAbrir()
        com.receiver = door
        door.addCommand(com)

        l1.putElementOn(ori1x, door)
        l2.putElementOn(ori2x, door)

    def fabricarPanEn(self, obj, ref):
        obj.addChild(self.fabricarPan(ref))
    
    def fabricarPocionEn(self, obj, ref):
        obj.addChild(self.fabricarPocion(ref))

    def fabricarPared(self):
        return Pared()

    def fabricarNorte(self):
        return Norte.obtenerInstancia(self)
    
    def fabricarEste(self):
        return Este.obtenerInstancia(self)
    
    def fabricarOeste(self):
        return Oeste.obtenerInstancia(self)
    
    def fabricarSur(self):
        return Sur.obtenerInstancia(self)
    
    def fabricarBomba(self):
        return Bomba()
    
    def fabricarFuego(self):
        return Fuego()
    
    def fabricarBatePinchos(self):
        return BatePinchos()