import unittest
import sys
from io import StringIO
import os
from pathlib import Path


from LaberintoBuilder.Director import Director
from Ente.Character import Character

class Test_Triangulo(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save = sys.stdout
        sys.stdout = StringIO()  # Deshabilitamos la salida para facilitar la lectura de los test
        json_file = Path('json') / 'maze3hab-tri.json'
        if not json_file.exists():
            raise FileNotFoundError(f"El archivo {json_file} no se encuentra.")
        
        director = Director()
        director.procesar(str(json_file))
        self.juego = director.getJuego()
        personaje = Character()
        personaje.seudonimo = "Juan"
        self.juego.agregarPersonaje(personaje)
        sys.stdout = sys.stdout_save  # Volvemos a habilitarla

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(), True)
        self.assertEqual(len(self.juego.laberinto.objChildren), 3)
        print("TEST INICIAL SUPERADO.\n")

    def testHabitaciones(self):
        # Habitación 1
        hab1 = self.juego.laberinto.objChildren[0]
        self.assertEqual(hab1.esHabitacion(), True)
        self.assertEqual(hab1.ref, 1)
        self.assertEqual(len(hab1.objChildren), 3)
        self.assertEqual(hab1.form.esTriangulo(), True)
        self.assertEqual(hab1.form.norte.esPuerta(), True)
        self.assertEqual(hab1.form.este.esPared(), True)
        self.assertEqual(hab1.form.oeste.esPuerta(), True)
        # Habitación 2
        hab2 = self.juego.laberinto.objChildren[1]
        self.assertEqual(hab2.esHabitacion(), True)
        self.assertEqual(hab2.ref, 2)
        self.assertEqual(len(hab2.objChildren), 2)
        self.assertEqual(hab2.form.esTriangulo(), True)
        self.assertEqual(hab2.form.norte.esPared(), True)
        self.assertEqual(hab2.form.este.esPuerta(), True)
        self.assertEqual(hab2.form.oeste.esPuerta(), True)
        # Habitación 3
        hab3 = self.juego.laberinto.objChildren[2]
        self.assertEqual(hab3.esHabitacion(), True)
        self.assertEqual(hab3.ref, 3)
        self.assertEqual(len(hab3.objChildren), 3)
        self.assertEqual(hab3.form.esTriangulo(), True)
        self.assertEqual(hab3.form.norte.esPuerta(), True)
        self.assertEqual(hab3.form.este.esPuerta(), True)
        self.assertEqual(hab3.form.oeste.esPared(), True)

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")

    def testBichos(self):
        bichos = self.juego.bichos
        # Bicho 1
        b1 = bichos[0]
        self.assertEqual(b1.numero_identificador, 1)
        self.assertEqual(b1.modo.esAgresivo(), True)
        self.assertEqual(b1.posicion, self.juego.laberinto.objChildren[0])
        self.assertEqual(b1.juego, self.juego)
        self.assertEqual(b1.estado.estaVivo(), True)
        # Bicho 2
        b2 = bichos[1]
        self.assertEqual(b2.numero_identificador, 2)
        self.assertEqual(b2.modo.esPerezoso(), True)
        self.assertEqual(b2.posicion, self.juego.laberinto.objChildren[1])
        self.assertEqual(b2.juego, self.juego)
        self.assertEqual(b2.estado.estaVivo(), True)
        # Bicho 3
        b3 = bichos[2]
        self.assertEqual(b3.numero_identificador, 3)
        self.assertEqual(b3.modo.esAgresivo(), True)
        self.assertEqual(b3.posicion, self.juego.laberinto.objChildren[2])
        self.assertEqual(b3.juego, self.juego)
        self.assertEqual(b3.estado.estaVivo(), True)

        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.prota
        self.assertEqual(personaje.seudonimo, "Juan")
        self.assertEqual(personaje.posicion, self.juego.getHab(1))
        self.assertEqual(personaje.estado.estaVivo(), True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.mochila.esMochila(), True)
        self.assertEqual(len(personaje.mochila.children), 0)
        self.assertEqual(personaje.cuerpo.esCuerpo(), True)
        self.assertEqual(personaje.cuerpo.brazoAtaque is None, True)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        # Puerta 1
        p1 = self.juego.getHab(1).form.norte
        self.assertEqual(p1.esPuerta(), True)
        self.assertEqual(p1.lado1, self.juego.getHab(1))
        self.assertEqual(p1.lado2, self.juego.getHab(2))
        self.assertEqual(p1.commands[0].esAbrir(), True)
        self.assertEqual(p1.commands[0].receiver, p1)
        # Puerta 2
        p2 = self.juego.getHab(2).form.oeste
        self.assertEqual(p2.esPuerta(), True)
        self.assertEqual(p2.lado1, self.juego.getHab(2))
        self.assertEqual(p2.lado2, self.juego.getHab(3))
        self.assertEqual(p2.commands[0].esAbrir(), True)
        self.assertEqual(p2.commands[0].receiver, p2)
        # Puerta 3
        p3 = self.juego.getHab(3).form.este
        self.assertEqual(p3.esPuerta(), True)
        self.assertEqual(p3.lado1, self.juego.getHab(3))
        self.assertEqual(p3.lado2, self.juego.getHab(1))
        self.assertEqual(p3.commands[0].esAbrir(), True)
        self.assertEqual(p3.commands[0].receiver, p3)
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        # Armario 1
        arm1 = None
        pad1 = None
        for hijo in (pad1 := self.juego.getHab(1)).objChildren:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.ref, 1)
        self.assertEqual(arm1.padre, pad1)
        self.assertEqual(len(arm1.objChildren), 1)
        self.assertEqual(arm1.form.esTriangulo(), True)
        self.assertEqual(arm1.form.norte.esPared(), True)
        self.assertEqual(arm1.form.este.esPared(), True)
        self.assertEqual(arm1.form.oeste.esPuerta(), True)
        self.assertEqual((p1 := arm1.form.oeste).esPuerta(), True)
        self.assertEqual(p1.estaAbierta(), False)
        self.assertEqual(p1.commands[0].esAbrir(), True)
        self.assertEqual(p1.commands[0].receiver, p1)

        # Armario 2
        arm2 = None
        pad3 = None
        for hijo in (pad3 := self.juego.getHab(3)).objChildren:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.ref, 3)
        self.assertEqual(arm2.padre, pad3)
        self.assertEqual(len(arm2.objChildren), 2)
        self.assertEqual(arm2.form.esTriangulo(), True)
        self.assertEqual(arm2.form.norte.esPared(), True)
        self.assertEqual(arm2.form.este.esPared(), True)
        self.assertEqual(arm2.form.oeste.esPuerta(), True)
        self.assertEqual((p2 := arm2.form.oeste).esPuerta(), True)
        self.assertEqual(p2.estaAbierta(), False)
        self.assertEqual(p2.commands[0].esAbrir(), True)
        self.assertEqual(p2.commands[0].receiver, p2)

        print("\nTEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        tunel = None
        pad3 = None
        for hijo in (pad3 := self.juego.getHab(3)).objChildren:
            if hijo.esTunel():
                tunel = hijo
        self.assertEqual(tunel is not None, True)
        self.assertEqual(tunel.padre, pad3)
        print("TEST DE TUNELES SUPERADO.")

    def testbombas(self):
        # Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1 := self.juego.getHab(1)).objChildren:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num, 1)
        self.assertEqual(bomba1.activa, True)
        self.assertEqual(bomba1.padre, pad1)
        self.assertEqual(bomba1.commands[0].esEntrar(), True)
        self.assertEqual(bomba1.commands[0].receiver, bomba1)

    def testfuegos(self):
        # Fuego 1
        fuego = None
        pad1 = None
        for hijo in (pad1 := self.juego.getHab(1)).objChildren:
            if hijo.esFuego():
                fuego = hijo
        self.assertEqual(fuego.num, 1)
        self.assertEqual(fuego.activo, True)
        self.assertEqual(fuego.padre, pad1)
        self.assertEqual(fuego.commands[0].esEntrar(), True)
        self.assertEqual(fuego.commands[0].receiver, fuego)

        # Fuego 2
        fuego2 = None
        pad2 = None
        for hijo in (pad2 := self.juego.getHab(2)).objChildren:
            if hijo.esFuego():
                fuego2 = hijo
        self.assertEqual(fuego2.num, 1)
        self.assertEqual(fuego2.activo, True)
        self.assertEqual(fuego2.padre, pad2)
        self.assertEqual(fuego2.commands[0].esEntrar(), True)
        self.assertEqual(fuego2.commands[0].receiver, fuego2)

    def testFuegoDamage(self):
        personaje = self.juego.prota
        for hijo in (pad1 := self.juego.getHab(1)).objChildren:
            if hijo.esFuego():
                fuego = hijo
        
        vida_inicial = personaje.corazones
        print("Vida antes de quemarse: ", vida_inicial)
        fuego.entrar(personaje)
        print("Vida despues de quemarse: ", personaje.corazones)
        self.assertLess(personaje.corazones, vida_inicial)
        print("TEST DE DAÑO POR FUEGO SUPERADO.\n")

    def testApagarFuego(self):
        # Fuego 2
        hab2 = self.juego.getHab(2)
        fuego2 = None
        fuego_final = None
        pad2 = None
        for hijo in (pad2 := hab2).objChildren:
            if hijo.esFuego():
                fuego2 = hijo
        self.assertEqual(fuego2.num, 1)
        self.assertEqual(fuego2.activo, True)
        self.assertEqual(fuego2.padre, pad2)
        self.assertEqual(fuego2.commands[0].esEntrar(), True)
        self.assertEqual(fuego2.commands[0].receiver, fuego2)

        # Apagar el fuego en la habitación 2
        for hijo in hab2.objChildren:
            if hijo.esFuego():
                hijo.apagarFuego()

        for hijo in (pad2 := hab2).objChildren:
            if hijo.esFuego():
                fuego_final = hijo
        self.assertEqual(fuego_final.num, 1)
        self.assertEqual(fuego_final.activo, False)
        print("TEST DE APAGAR FUEGO SUPERADO.\n")


    def testObjetos(self):
        # Objetos Habitación 1
        hab1 = self.juego.getHab(1)
        # pan 1
        arm1 = hab1.objChildren[0]
        self.assertEqual((pan1 := arm1.objChildren[0]).esPan(), True)
        self.assertEqual((com1 := pan1.commands[0]).esCoger(), True)
        self.assertEqual(com1.receiver, pan1)

        # Objetos Habitación 2
        hab2 = self.juego.getHab(2)
        # Katana 1
        self.assertEqual((BatePinchos1 := hab2.objChildren[0]).esBatePinchos(), True)
        self.assertEqual(BatePinchos1.ref, 1)
        self.assertEqual(BatePinchos1.commands[0].esCoger(), True)
        self.assertEqual(BatePinchos1.commands[0].receiver, BatePinchos1)

        # Objetos Habitación 3
        hab3 = self.juego.getHab(3)
        arm3 = hab3.objChildren[1]
        # Poción 1
        self.assertEqual((pocion1 := arm3.objChildren[0]).esPocion(), True)
        self.assertEqual((com1 := pocion1.commands[0]).esCoger(), True)
        self.assertEqual(com1.receiver, pocion1)
        # Poción 2
        self.assertEqual((pocion2 := arm3.objChildren[1]).esPocion(), True)
        self.assertEqual((com1 := pocion2.commands[0]).esCoger(), True)
        self.assertEqual(com1.receiver, pocion2)
        # Katana 2
        self.assertEqual((Katana2 := hab3.objChildren[0]).esBatePinchos(), True)
        self.assertEqual(Katana2.ref, 1)
        self.assertEqual(Katana2.commands[0].esCoger(), True)
        self.assertEqual(Katana2.commands[0].receiver, Katana2)

        print("TEST DE OBJETOS SUPERADO.\n")

if __name__ == '__main__':
    unittest.main()
