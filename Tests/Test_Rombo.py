import unittest
import sys
from io import StringIO
from pathlib import Path

from LaberintoBuilder.Director import Director
from Ente.Character import Character

class Test_Rombo(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.stdout_save = sys.stdout
        sys.stdout = StringIO()  # Deshabilitamos la salida para facilitar la lectura de los test
        
        json_file = Path('json') / 'maze4hab-diam.json'
        if not json_file.exists():
            raise FileNotFoundError(f"El archivo {json_file} no se encuentra.")
        
        director = Director()
        director.procesar(str(json_file))
        self.juego = director.getJuego()
        
        personaje = Character()
        personaje.seudonimo = "Jorge"
        self.juego.agregarPersonaje(personaje)
        
        sys.stdout = self.stdout_save  # Volvemos a habilitarla

    def tearDown(self):
        sys.stdout = self.stdout_save

    def testIniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertTrue(self.juego.esJuego())
        self.assertEqual(len(self.juego.laberinto.objChildren), 4)
        print("TEST INICIAL SUPERADO.\n")

    def testHabitaciones(self):
        hab1 = self.juego.laberinto.objChildren[0]
        self.assertTrue(hab1.esHabitacion())
        self.assertEqual(hab1.ref, 1)
        self.assertEqual(len(hab1.objChildren), 1)
        self.assertTrue(hab1.form.esRombo())
        self.assertTrue(hab1.form.noreste.esPuerta())
        self.assertTrue(hab1.form.noroeste.esPared())
        self.assertTrue(hab1.form.sureste.esPuerta())
        self.assertTrue(hab1.form.suroeste.esPared())
        
        hab2 = self.juego.laberinto.objChildren[1]
        self.assertTrue(hab2.esHabitacion())
        self.assertEqual(hab2.ref, 2)
        self.assertEqual(len(hab2.objChildren), 2)
        self.assertTrue(hab2.form.esRombo())
        self.assertTrue(hab2.form.noreste.esPuerta())
        self.assertTrue(hab2.form.noroeste.esPuerta())
        self.assertTrue(hab2.form.sureste.esPared())
        self.assertTrue(hab2.form.suroeste.esPared())
        
        hab3 = self.juego.laberinto.objChildren[2]
        self.assertTrue(hab3.esHabitacion())
        self.assertEqual(hab3.ref, 3)
        self.assertEqual(len(hab3.objChildren), 1)
        self.assertTrue(hab3.form.esRombo())
        self.assertTrue(hab3.form.noreste.esPared())
        self.assertTrue(hab3.form.noroeste.esPared())
        self.assertTrue(hab3.form.sureste.esPuerta())
        self.assertTrue(hab3.form.suroeste.esPuerta())
        
        hab4 = self.juego.laberinto.objChildren[3]
        self.assertTrue(hab4.esHabitacion())
        self.assertEqual(hab4.ref, 4)
        self.assertEqual(len(hab4.objChildren), 0)
        self.assertTrue(hab4.form.esRombo())
        self.assertTrue(hab4.form.noreste.esPared())
        self.assertTrue(hab4.form.noroeste.esPuerta())
        self.assertTrue(hab4.form.sureste.esPared())
        self.assertTrue(hab4.form.suroeste.esPuerta())

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")

    def testBichos(self):
        bichos = self.juego.bichos
        
        b1 = bichos[0]
        self.assertEqual(b1.numero_identificador, 1)
        self.assertTrue(b1.modo.esAgresivo())
        self.assertEqual(b1.posicion, self.juego.laberinto.objChildren[0])
        self.assertEqual(b1.juego, self.juego)
        self.assertTrue(b1.estado.estaVivo())
        
        b2 = bichos[1]
        self.assertEqual(b2.numero_identificador, 2)
        self.assertTrue(b2.modo.esPerezoso())
        self.assertEqual(b2.posicion, self.juego.laberinto.objChildren[3])
        self.assertEqual(b2.juego, self.juego)
        self.assertTrue(b2.estado.estaVivo())
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.prota
        self.assertEqual(personaje.seudonimo, "Jorge")
        self.assertEqual(personaje.posicion, self.juego.getHab(1))
        self.assertTrue(personaje.estado.estaVivo())
        self.assertEqual(personaje.juego, self.juego)
        self.assertTrue(personaje.mochila.esMochila())
        self.assertEqual(len(personaje.mochila.children), 0)
        self.assertTrue(personaje.cuerpo.esCuerpo())
        self.assertIsNone(personaje.cuerpo.brazoAtaque)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        p1 = self.juego.getHab(1).form.sureste
        self.assertTrue(p1.esPuerta())
        self.assertEqual(p1.lado1, self.juego.getHab(1))
        self.assertEqual(p1.lado2, self.juego.getHab(2))
        self.assertTrue(p1.commands[0].esAbrir())
        self.assertEqual(p1.commands[0].receiver, p1)
        
        p2 = self.juego.getHab(2).form.noreste
        self.assertTrue(p2.esPuerta())
        self.assertEqual(p2.lado1, self.juego.getHab(2))
        self.assertEqual(p2.lado2, self.juego.getHab(4))
        self.assertTrue(p2.commands[0].esAbrir())
        self.assertEqual(p2.commands[0].receiver, p2)
        
        p3 = self.juego.getHab(4).form.noroeste
        self.assertTrue(p3.esPuerta())
        self.assertEqual(p3.lado1, self.juego.getHab(4))
        self.assertEqual(p3.lado2, self.juego.getHab(3))
        self.assertTrue(p3.commands[0].esAbrir())
        self.assertEqual(p3.commands[0].receiver, p3)
        
        p4 = self.juego.getHab(3).form.suroeste
        self.assertTrue(p4.esPuerta())
        self.assertEqual(p4.lado1, self.juego.getHab(3))
        self.assertEqual(p4.lado2, self.juego.getHab(1))
        self.assertTrue(p4.commands[0].esAbrir())
        self.assertEqual(p4.commands[0].receiver, p4)
        
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        arm1 = None
        pad1 = self.juego.getHab(1)
        for hijo in pad1.objChildren:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.ref, 1)
        self.assertEqual(arm1.padre, pad1)
        self.assertEqual(len(arm1.objChildren), 3)
        self.assertTrue(arm1.form.esRombo())
        self.assertTrue(arm1.form.noroeste.esPared())
        self.assertTrue(arm1.form.noreste.esPared())
        self.assertTrue(arm1.form.sureste.esPared())
        self.assertTrue((p1 := arm1.form.suroeste).esPuerta())
        self.assertFalse(p1.estaAbierta())
        self.assertTrue(p1.commands[0].esAbrir())
        self.assertEqual(p1.commands[0].receiver, p1)

        arm2 = None
        pad2 = self.juego.getHab(2)
        for hijo in pad2.objChildren:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.ref, 2)
        self.assertEqual(arm2.padre, pad2)
        self.assertEqual(len(arm2.objChildren), 1)
        self.assertTrue(arm2.form.esRombo())
        self.assertTrue(arm2.form.noroeste.esPared())
        self.assertTrue(arm2.form.noreste.esPared())
        self.assertTrue(arm2.form.sureste.esPared())
        self.assertTrue((p2 := arm2.form.suroeste).esPuerta())
        self.assertFalse(p2.estaAbierta())
        self.assertTrue(p2.commands[0].esAbrir())
        self.assertEqual(p2.commands[0].receiver, p2)

        print("TEST DE ARMARIOS SUPERADO.")
    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.getHab(1)
        #pan 1
        arm1 = hab1.objChildren[0]
        self.assertEqual((pan1:=arm1.objChildren[0]).esPan(),True)
        self.assertEqual((com1:=pan1.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pan1)
        #pan 2
        self.assertEqual((pan2:=arm1.objChildren[1]).esPan(),True)
        self.assertEqual((com1:=pan2.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pan2)
        # Poción 1
        self.assertEqual((pocion1:=arm1.objChildren[2]).esPocion(),True)
        self.assertEqual((com1:=pocion1.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pocion1)

        #Objetos Habitación 2
        hab2 = self.juego.getHab(2)
        arm2 = hab2.objChildren[1]
        # Poción 2
        self.assertEqual((pocion2:=arm2.objChildren[0]).esPocion(),True)
        self.assertEqual((com1:=pocion2.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pocion2)
        #Katana metal
        self.assertEqual((BatePinchos1:=hab2.objChildren[0]).esBatePinchos(),True)
        self.assertEqual(BatePinchos1.ref,1)
        self.assertEqual(BatePinchos1.commands[0].esCoger(),True)
        self.assertEqual(BatePinchos1.commands[0].receiver,BatePinchos1)
        print("TEST DE OBJETOS SUPERADO.\n")
        
if __name__ == '__main__':
    unittest.main()