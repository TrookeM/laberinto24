import unittest
import sys
from io import StringIO
import os
sys.path.append('C:\\Users\\yorch\\Desktop\\PLaberinto\\laberinto24\\json')

from LaberintoBuilder.Director import Director
from Ente.Character import Character
class Second_test(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save =sys.stdout
        sys.stdout = StringIO()#Deshabilitamos la salida para facilitar la lectura de los test
        director = Director()
        director.procesar('maze4hab-diam.json')
        self.juego = director.getJuego()
        personaje = Character()
        personaje.seudonimo = "Jorge"
        self.juego.agregarPersonaje(personaje)
        sys.stdout=sys.stdout_save#Volvemos a habilitarla

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.objChildren),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        #Habitación 1
        hab1 = self.juego.laberinto.objChildren[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.ref,1)
        self.assertEqual(len(hab1.objChildren),1)
        self.assertEqual(hab1.form.esRombo(),True)
        self.assertEqual(hab1.form.noreste.esPuerta(),True)
        self.assertEqual(hab1.form.noroeste.esPared(),True)
        self.assertEqual(hab1.form.sureste.esPuerta(),True)
        self.assertEqual(hab1.form.suroeste.esPared(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.objChildren[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.ref,2)
        self.assertEqual(len(hab2.objChildren),2)
        self.assertEqual(hab2.form.esRombo(),True)
        self.assertEqual(hab2.form.noreste.esPuerta(),True)
        self.assertEqual(hab2.form.noroeste.esPuerta(),True)
        self.assertEqual(hab2.form.sureste.esPared(),True)
        self.assertEqual(hab2.form.suroeste.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.objChildren[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.ref,3)
        self.assertEqual(len(hab3.objChildren),1)
        self.assertEqual(hab3.form.esRombo(),True)
        self.assertEqual(hab3.form.noreste.esPared(),True)
        self.assertEqual(hab3.form.noroeste.esPared(),True)
        self.assertEqual(hab3.form.sureste.esPuerta(),True)
        self.assertEqual(hab3.form.suroeste.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.objChildren[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.ref,4)
        self.assertEqual(len(hab4.objChildren),0)
        self.assertEqual(hab4.form.esRombo(),True)
        self.assertEqual(hab4.form.noreste.esPared(),True)
        self.assertEqual(hab4.form.noroeste.esPuerta(),True)
        self.assertEqual(hab4.form.sureste.esPared(),True)
        self.assertEqual(hab4.form.suroeste.esPuerta(),True)

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")


    def testBichos(self):
        bichos = self.juego.bichos
        #Bicho 1
        b1 = bichos[0]
        self.assertEqual(b1.numero_identificador,1)
        self.assertEqual(b1.modo.esAgresivo(),True)
        self.assertEqual(b1.posicion,self.juego.laberinto.objChildren[0])
        self.assertEqual(b1.juego,self.juego)
        self.assertEqual(b1.estado.estaVivo(),True)
        #Bicho 2
        b2 = bichos[1]
        self.assertEqual(b2.numero_identificador,2)
        self.assertEqual(b2.modo.esPerezoso(),True)
        self.assertEqual(b2.posicion,self.juego.laberinto.objChildren[3])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.prota
        self.assertEqual(personaje.seudonimo,"Jorge")
        self.assertEqual(personaje.posicion,self.juego.getHab(1))
        self.assertEqual(personaje.estado.estaVivo(),True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.mochila.esMochila(),True)
        self.assertEqual(len(personaje.mochila.children),0)
        self.assertEqual(personaje.cuerpo.esCuerpo(),True)
        self.assertEqual(personaje.cuerpo.brazoAtaque is None, True)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        #Puerta 1
        p1 = self.juego.getHab(1).form.sureste
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.getHab(1))
        self.assertEqual(p1.lado2,self.juego.getHab(2))
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        #Puerta 2
        p2 = self.juego.getHab(2).form.noreste
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.getHab(2))
        self.assertEqual(p2.lado2,self.juego.getHab(4))
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        #Puerta 3
        p3 = self.juego.getHab(4).form.noroeste
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.getHab(4))
        self.assertEqual(p3.lado2,self.juego.getHab(3))
        self.assertEqual(p3.commands[0].esAbrir(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        #Puerta 4
        p4 = self.juego.getHab(3).form.suroeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.getHab(3))
        self.assertEqual(p4.lado2,self.juego.getHab(1))
        self.assertEqual(p4.commands[0].esAbrir(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        #Armario 1
        arm1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.getHab(1)).objChildren:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.ref,1)
        self.assertEqual(arm1.padre,pad1)
        self.assertEqual(len(arm1.objChildren),3)
        self.assertEqual(arm1.form.esRombo(),True)
        self.assertEqual(arm1.form.noroeste.esPared(),True)
        self.assertEqual(arm1.form.noreste.esPared(),True)
        self.assertEqual(arm1.form.sureste.esPared(),True)
        self.assertEqual((p1:=arm1.form.suroeste).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)

        # Armario 2
        arm2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.getHab(2)).objChildren:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.ref, 2)
        self.assertEqual(arm2.padre, pad2)
        self.assertEqual(len(arm2.objChildren), 1)
        self.assertEqual(arm2.form.esRombo(), True)
        self.assertEqual(arm2.form.noroeste.esPared(), True)
        self.assertEqual(arm2.form.noreste.esPared(), True)
        self.assertEqual(arm2.form.sureste.esPared(), True)
        self.assertEqual((p2:=arm2.form.suroeste).esPuerta(), True)
        self.assertEqual(p2.estaAbierta(), False)
        self.assertEqual(p2.commands[0].esAbrir(), True)
        self.assertEqual(p2.commands[0].receiver, p2)

        print("TEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        pass#No tiene túneles
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.getHab(3)).objChildren:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.commands[0].esEntrar(),True)
        self.assertEqual(bomba1.commands[0].receiver,bomba1)

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