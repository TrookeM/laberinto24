from LaberintoBuilder.LaberintoBuilder import LaberintoBuilder
from LaberintoBuilder.LaberintoDiamondBuilder import LaberintoDiamondBuilder
from LaberintoBuilder.LaberintoTriangleBuilder import LaberintoTrianguleBuilder
import json

class Director():
    
    def __init__(self):
        self.builder = None
        self.diccionario = None
        self.form = None

    def procesar(self, input):

        self.readConfig(input)
        self.iniBuilder()
        self.makeMaze()
        self.makeJuego()
        self.createAntagonist()

    def getJuego(self):
        return self.builder.obtenerJuego()


    def readConfig(self,unArchivo):

        with open(unArchivo, 'r', encoding='utf8') as file:
            self.diccionario = json.load(file)

    def iniBuilder(self):
        if self.diccionario['forma'] == "cuadrado":
            self.form = "Cuadrado"
            self.builder = LaberintoBuilder()
        if self.diccionario['forma'] == "rombo":
            self.form = "Diamante"
            self.builder = LaberintoDiamondBuilder()
        if self.diccionario['forma'] == "triangulo":
            self.form = "Triangulo"
            self.builder = LaberintoTrianguleBuilder()

    def makeMaze(self):
        self.builder.fabricarLaberinto()

        for lab in self.diccionario['laberinto']:
            self.labRecursivo(lab,'root')

        for puerta in self.diccionario['puertas']:
            self.builder.fabricarPuertaL(puerta[0], puerta[1], puerta[2], puerta[3])

    def labRecursivo(self, dic, parent):
        if dic['tipo'] == 'habitacion':
            padre = self.builder.fabricarHabitacion(dic['num'])
        if dic['tipo'] == 'armario':
            padre = self.builder.fabricarArmarioEn(parent, dic['num'])
        
        if dic['tipo'] == 'bomba':
            padre = self.builder.fabricarBombaEn(parent, dic['num'])
        if dic['tipo'] == 'fuego':
            padre = self.builder.fabricarFuegoEn(parent, dic['num'])    
        if dic['tipo'] == 'tunel':
            padre = self.builder.fabricarTunelEn(parent)

        if dic['tipo'] == 'pan':
            padre = self.builder.fabricarPanEn(parent, dic['num'])
        if dic['tipo'] == 'pocion':
            padre = self.builder.fabricarPocionEn(parent, dic['num'])
        if dic['tipo'] == 'batepinchos':
            padre = self.builder.fabricarBatePinchosEn(parent, dic['num'])
        
        #Hijos
        hijos = dic.get('hijos',[])

        for h in hijos:
            self.labRecursivo(h, padre)


    def makeJuego(self):
        self.builder.makeJuego()

    def createAntagonist(self):
        antagonistas = self.diccionario.get('bichos',[])

        for ant in antagonistas:
            self.builder.fabricarBichoAlternativo(ant['modo'], ant['posicion'])