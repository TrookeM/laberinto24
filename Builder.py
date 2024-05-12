import json
import keyboard
import time

from Juego import Juego
from Laberinto import Laberinto, Habitacion, Puerta, Pared, Bomba, Rectangulo, Hexagono, Norte, Este, Sur, Oeste, Noreste, Sureste, Suroeste, Noroeste
from Bicho import Bestia, Agresiva, Perezosa


class Director:
    def __init__(self):
        self.dict = None
        self.builder = LaberintoBuilder()

    def procesar(self, filename):
        self.leer_archivo(filename)
        self.crear_laberinto()
        self.crear_game()
        self.crear_bestias()

    def leer_archivo(self, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
                self.dict = data
        except FileNotFoundError:
            print(f"File {filename} does not exist")
            return None

    def getGame(self):
        return self.builder.getGame()
    
    def iniBuilder(self):
        if (self.dict['form'] == 'rectangle'):
            self.builder=LaberintoBuilder()
        elif (self.dict['form'] == 'hexagon'):
            self.builder=LaberintoHexagonalBuilder()
        else:
            print("Form not found")
            return None

    def crear_game(self):
        self.builder.makeGame()

    def crear_laberinto(self):
        self.builder.makelaberinto()

        for each in self.dict['laberinto']:
            self.crear_laberinto_recursivo(each, 'root')

        for each in self.dict['puertas']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.makepuerta(n1, or1, n2, or2)

    def crear_laberinto_recursivo(self, un_dic, padre):

        if un_dic['tipo'] == 'habitacion':
            con = self.builder.makehabitacion(un_dic['num'])

        if un_dic['tipo'] == 'bomba':
            self.builder.makebombaIn(padre)

        if 'hijos' in un_dic:
            for each in un_dic['hijos']:
                self.crear_laberinto_recursivo(each, con)

    def crear_bestias(self):
        for each in self.dict['bestias']:
            modo = each['modo']
            if modo == 'Aggressive':
                self.builder.makeAggressivebestiaPosition(each['posicion'])
            elif modo == 'Lazy':
                self.builder.makeLazybestiaPosition(each['posicion'])


class LaberintoBuilder:
    def __init__(self):
        self.game = None
        self.laberinto = None

    def getGame(self):
        return self.game

    def makeGame(self):
        self.game = Juego()
        self.game.prototipo = self.laberinto
        self.game.laberinto = self.game.clonarLaberinto()
        

    def makeForm(self):
        return Rectangulo()

    def makelaberinto(self):
        self.laberinto = Laberinto()

    def makeWall(self):
        return Pared()

    def makepuerta(self, habitacion1, habitacion2):
        puerta = Puerta(habitacion1, habitacion2)
        return puerta

    def makebombaIn(self, habitacion):
        bomba = Bomba()
        habitacion.addChild(bomba)
        return bomba

    def makehabitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.form = self.makeForm()
        #habitacion.addOrientation(self.makeNorte())
        #habitacion.addOrientation(self.makeEste())
        #habitacion.addOrientation(self.makeSur())
        #habitacion.addOrientation(self.makeOeste())
        for each in habitacion.getOrientations():
            each.setEMinOr(self.makeWall(), habitacion.form)
        self.laberinto.addhabitacion(habitacion)
        return habitacion

    def makeNorte(self):
        return Norte().get_instance()

    def makeEste(self):
        return Este.get_instance()

    def makeSur(self):
        return Sur().get_instance()

    def makeOeste(self):
        return Oeste().get_instance()

    def makepuerta(self, un_num, una_or_string, otro_num, otra_or_string):
        lado1 = self.laberinto.gethabitacion(un_num)
        lado2 = self.laberinto.gethabitacion(otro_num)

        or1 = getattr(self, 'make' + una_or_string)()
        or2 = getattr(self, 'make' + otra_or_string)()

        pt = Puerta(lado1, lado2)

        lado1.setEMinOr(pt, or1)
        lado2.setEMinOr(pt, or2)

    def makeAggressivebestia(self):
        return Bestia(Agresiva())

    def makeLazybestia(self):
        return Bestia(Perezosa())

    def makeAggressiveBestiaPosition(self, num):
        habitacion = self.laberinto.gethabitacion(num)
        bestia = self.makeAggressivebestia()
        bestia.position = habitacion
        self.game.addbestia(bestia)

    def makeLazyBestiaPosition(self, num):
        habitacion = self.laberinto.gethabitacion(num)
        bestia = self.makeLazybestia()
        bestia.position = habitacion
        self.game.addbestia(bestia)

class LaberintoHexagonalBuilder(LaberintoBuilder):
    def makeForm(self):
        return Hexagono()
    
    def makehabitacion(self):
        habitacion = habitacion()
        habitacion.form = self.makeForm()                           
        for each in habitacion.getOrientations():
            each.setEMinOr(self.makeWall(), habitacion.form)
        self.laberinto.addhabitacion(habitacion)
        return habitacion


def main(): #stdscr
    # Turn off cursor blinking
    #curses.curs_set(0)
    # Enable keypad mode
    #stdscr.keypad(True)

    director=Director()
    
    director.procesar('C:\\Users\\yorch\\laberintos\\laberinto2habitacion.json')

    game=director.getGame()
    game.addPerson("Juan")
    person=game.person
    game.openpuertas()
    game.launchThreds()
    
    #stdscr.clear()
    #stdscr.addstr("Press arrow keys or 'q' to quit.\n")
    
    
    while True:
        if keyboard.is_pressed('q'):
            break  # Exit the program
        elif keyboard.is_pressed("w"): #curses.KEY_UP:
            #stdscr.addstr("Up Arrow Pressed\n")
            person.goNorte()
        elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
            #stdscr.addstr("Down Arrow Pressed\n")
            person.goSur()
        elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
            #stdscr.addstr("Left Arrow Pressed\n")
            person.goOeste()
        elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
            #stdscr.addstr("Right Arrow Pressed\n")
            person.goEste()
        elif keyboard.is_pressed("enter"):#curses.KEY_ENTER or key in [10, 13]:
            #stdscr.addstr("Enter Pressed\n")
            person.attack()
        #else:
            #stdscr.addstr("Key Pressed: {}\n".format(chr(key)))
    game.stopThreds()
    # Clean up
    #curses.curs_set(1)
    #stdscr.keypad(False)
    
#main()
