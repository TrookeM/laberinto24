from Forma.Triangle import Triangle
from LaberintoBuilder.LaberintoBuilder import LaberintoBuilder
from ElementoMapa.Container.Habitacion import Habitacion
from Orientaciones.Norte import Norte
from Orientaciones.Este import Este
from Orientaciones.Oeste import Oeste
from Command.Abrir import Abrir

class LaberintoTrianguleBuilder(LaberintoBuilder):
    
    def fabricarForma(self):
        return Triangle()
    
    def fabricarNorte(self):
        return Norte.obtenerInstancia()
    
    def fabricarEste(self):
        return Este.obtenerInstancia()
    
    def fabricarOeste(self):
        return Oeste.obtenerInstancia()
    
    def fabricarHabitacion(self, num):
        hab = Habitacion(num)

        forma = self.fabricarForma()
        forma.ref = num
        hab.form = forma

        hab.putElementOn(self.fabricarNorte(), self.fabricarPared())
        hab.putElementOn(self.fabricarEste(), self.fabricarPared())
        hab.putElementOn(self.fabricarOeste(), self.fabricarPared())

        hab.addOr(self.fabricarNorte())
        hab.addOr(self.fabricarEste())
        hab.addOr(self.fabricarOeste())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
    def fabricarArmarioEn(self, padre, num):
        armario = self.fabricarArmario(num)
        
        p1 = self.fabricarPuerta()
        cmd = Abrir()
        cmd.receiver = p1

        p1.addCommand(cmd)

        p1.lado1 = armario
        p1.lado2 = padre

        armario.form = self.fabricarForma()

        armario.addOr(self.fabricarNorte())
        armario.addOr(self.fabricarEste())
        armario.addOr(self.fabricarOeste())

        armario.putElementOn(self.fabricarNorte(), self.fabricarPared())
        armario.putElementOn(self.fabricarEste(), self.fabricarPared())
        armario.putElementOn(self.fabricarOeste(), p1)

        padre.addChild(armario)
        return armario
