import unittest
import os
from io import StringIO
import sys
from pathlib import Path

from LaberintoBuilder.Director import Director
from Ente.Character import Character

class Test_Cuadrado(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.stdout_save = sys.stdout
        sys.stdout = StringIO()
        
        json_file = Path('json') / 'maze4hab.json'
        if not json_file.exists():
            raise FileNotFoundError(f"El archivo {json_file} no se encuentra.")
        
        director = Director()
        director.procesar(str(json_file))
        self.juego = director.getJuego()
        
        personaje = Character()
        personaje.seudonimo = "Juan"
        self.juego.agregarPersonaje(personaje)
        
        sys.stdout = self.stdout_save

    def tearDown(self):
        sys.stdout = self.stdout_save

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.objChildren),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        hab1 = self.juego.laberinto.objChildren[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.ref,1)
        self.assertEqual(len(hab1.objChildren),2)
        self.assertEqual(hab1.form.esCuadrado(),True)
        self.assertEqual(hab1.form.norte.esPared(),True)
        self.assertEqual(hab1.form.este.esPuerta(),True)
        self.assertEqual(hab1.form.oeste.esPared(),True)
        self.assertEqual(hab1.form.sur.esPuerta(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.objChildren[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.ref,2)
        self.assertEqual(len(hab2.objChildren),1)
        self.assertEqual(hab2.form.esCuadrado(),True)
        self.assertEqual(hab2.form.norte.esPuerta(),True)
        self.assertEqual(hab2.form.este.esPuerta(),True)
        self.assertEqual(hab2.form.oeste.esPared(),True)
        self.assertEqual(hab2.form.sur.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.objChildren[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.ref,3)
        self.assertEqual(len(hab3.objChildren),3)
        self.assertEqual(hab3.form.esCuadrado(),True)
        self.assertEqual(hab3.form.norte.esPared(),True)
        self.assertEqual(hab3.form.este.esPared(),True)
        self.assertEqual(hab3.form.oeste.esPuerta(),True)
        self.assertEqual(hab3.form.sur.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.objChildren[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.ref,4)
        self.assertEqual(len(hab4.objChildren),2)
        self.assertEqual(hab4.form.esCuadrado(),True)
        self.assertEqual(hab4.form.norte.esPuerta(),True)
        self.assertEqual(hab4.form.este.esPared(),True)
        self.assertEqual(hab4.form.oeste.esPuerta(),True)
        self.assertEqual(hab4.form.sur.esPared(),True)

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
        self.assertEqual(b2.posicion,self.juego.laberinto.objChildren[1])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        #Bicho 3
        b3 = bichos[2]
        self.assertEqual(b3.numero_identificador,3)
        self.assertEqual(b3.modo.esAgresivo(),True)
        self.assertEqual(b3.posicion,self.juego.laberinto.objChildren[2])
        self.assertEqual(b3.juego,self.juego)
        self.assertEqual(b3.estado.estaVivo(),True)
        #Bicho 4
        b4 = bichos[3]
        self.assertEqual(b4.numero_identificador,4)
        self.assertEqual(b4.modo.esPerezoso(),True)
        self.assertEqual(b4.posicion,self.juego.laberinto.objChildren[3])
        self.assertEqual(b4.juego,self.juego)
        self.assertEqual(b4.estado.estaVivo(),True)
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.prota
        self.assertEqual(personaje.seudonimo,"Juan")
        self.assertEqual(personaje.posicion,self.juego.getHab(1))
        self.assertEqual(personaje.estado.estaVivo(),True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.mochila.esMochila(),True)
        self.assertEqual(personaje.cuerpo.esCuerpo(),True)
        self.assertEqual(personaje.cuerpo.brazoAtaque is None, True)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        #Puerta 1
        p1 = self.juego.getHab(1).form.sur
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.getHab(1))
        self.assertEqual(p1.lado2,self.juego.getHab(2))
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(p1.estaAbierta(),False)
        #Puerta 2
        p2 = self.juego.getHab(2).form.este
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.getHab(2))
        self.assertEqual(p2.lado2,self.juego.getHab(4))
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(p2.estaAbierta(),False)
        #Puerta 3
        p3 = self.juego.getHab(4).form.norte
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.getHab(4))
        self.assertEqual(p3.lado2,self.juego.getHab(3))
        self.assertEqual(p3.commands[0].esAbrir(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(p3.estaAbierta(),False)
        #Puerta 4
        p4 = self.juego.getHab(3).form.oeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.getHab(3))
        self.assertEqual(p4.lado2,self.juego.getHab(1))
        self.assertEqual(p4.commands[0].esAbrir(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        self.assertEqual(p4.estaAbierta(),False)
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
        self.assertEqual(len(arm1.objChildren),1)
        self.assertEqual(arm1.form.esCuadrado(),True)
        self.assertEqual(arm1.form.norte.esPared(),True)
        self.assertEqual(arm1.form.este.esPared(),True)
        self.assertEqual((p1:=arm1.form.sur).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        #Armario 2
        arm2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.getHab(4)).objChildren:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.ref,2)
        self.assertEqual(arm2.padre,pad2)
        self.assertEqual(len(arm2.objChildren),0)
        self.assertEqual(arm2.form.esCuadrado(),True)
        self.assertEqual(arm2.form.norte.esPared(),True)
        self.assertEqual(arm2.form.este.esPared(),True)
        self.assertEqual(arm2.form.oeste.esPared(),True)
        self.assertEqual((p2:=arm1.form.sur).esPuerta(),True)
        self.assertEqual(p2.estaAbierta(),False)
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)

        # Armario 3
        arm3 = None
        pad3 = None
        for hijo in (pad3:=self.juego.getHab(3)).objChildren:
            if hijo.esArmario():
                arm3 = hijo
        self.assertEqual(arm3.ref, 3)
        self.assertEqual(arm3.padre, pad3)
        self.assertEqual(len(arm3.objChildren), 2)
        self.assertEqual(arm3.form.esCuadrado(), True)
        self.assertEqual(arm3.form.norte.esPared(), True)
        self.assertEqual(arm3.form.este.esPared(), True)
        self.assertEqual(arm3.form.oeste.esPared(), True)
        self.assertEqual((p3:=arm3.form.sur).esPuerta(), True)
        self.assertEqual(p3.estaAbierta(), False)
        self.assertEqual(p3.commands[0].esAbrir(), True)
        self.assertEqual(p3.commands[0].receiver, p3)


        print("TEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        tunel = None
        padre = None
        for hijo in (padre:=self.juego.getHab(3)).objChildren:
            if hijo.esTunel():
                tunel = hijo
        self.assertEqual(tunel.padre,padre)
        self.assertEqual(tunel.laberinto,None)
        print("TEST DE TÚNELES SUPERADO.\n")
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.getHab(1)).objChildren:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.commands[0].esEntrar(),True)
        self.assertEqual(bomba1.commands[0].receiver,bomba1)
        #Bomba 2
        bomba2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.getHab(4)).objChildren:
            if hijo.esBomba():
                bomba2 = hijo
        self.assertEqual(bomba2.num,2)
        self.assertEqual(bomba2.activa,True)
        self.assertEqual(bomba2.padre,pad2)
        self.assertEqual(bomba2.commands[0].esEntrar(),True)
        self.assertEqual(bomba2.commands[0].receiver,bomba2)
        print("TEST DE BOMBAS SUPERADO.")

    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.getHab(1)

        arm1 = hab1.objChildren[0]
        self.assertEqual((pan:=arm1.objChildren[0]).esPan(),True)
        self.assertEqual((com1:=pan.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pan)
        #Objetos Habitación 2
        hab2 = self.juego.getHab(2)
        self.assertEqual((BatePinchos1:=hab2.objChildren[0]).esBatePinchos(),True)
        self.assertEqual(BatePinchos1.ref,1)
        self.assertEqual(BatePinchos1.commands[0].esCoger(),True)
        self.assertEqual(BatePinchos1.commands[0].receiver,BatePinchos1)
        #Objetos Habitación 3
        hab3 = self.juego.getHab(3)
        arm3 = hab3.objChildren[1]
        #Pociones en el armario 3
        self.assertEqual((pocion1:=arm3.objChildren[0]).esPocion(),True)
        self.assertEqual((com1:=pocion1.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pocion1)
        self.assertEqual((pocion2:=arm3.objChildren[1]).esPocion(),True)
        self.assertEqual((com1:=pocion2.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,pocion2)
        #Katana
        self.assertEqual((Katana2:=hab3.objChildren[0]).esBatePinchos(),True)
        self.assertEqual(Katana2.ref,1)
        self.assertEqual(Katana2.commands[0].esCoger(),True)
        self.assertEqual(Katana2.commands[0].receiver,Katana2)
        print("TEST DE OBJETOS SUPERADO.\n")

    def testFuncionalidades(self):
        #Abrir puertas
        self.juego.openDoors()
        p1 = self.juego.getHab(1).form.sur
        p2 = self.juego.getHab(2).form.este
        p3 = self.juego.getHab(4).form.norte
        p4 = self.juego.getHab(3).form.oeste
        self.assertEqual(len(p1.commands),2)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.commands[0].esEntrar(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(p1.commands[1].esCerrar(),True)
        self.assertEqual(p1.commands[1].receiver,p1)
        self.assertEqual(len(p2.commands),2)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.commands[0].esEntrar(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(p2.commands[1].esCerrar(),True)
        self.assertEqual(p2.commands[1].receiver,p2)
        self.assertEqual(len(p3.commands),2)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.commands[0].esEntrar(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(p3.commands[1].esCerrar(),True)
        self.assertEqual(p3.commands[1].receiver,p3)
        self.assertEqual(len(p4.commands),2)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.commands[0].esEntrar(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        self.assertEqual(p4.commands[1].esCerrar(),True)
        self.assertEqual(p4.commands[1].receiver,p4)
        #Cerrar puertas
        self.juego.cerrarPuertas()
        print(p1.commands)
        self.assertEqual(len(p1.commands),1)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(len(p2.commands),1)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(len(p3.commands),1)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.commands[0].esAbrir(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(len(p4.commands),1)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.commands[0].esAbrir(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        #commands personaje posición Habitación 1
        personaje = self.juego.prota
        self.assertEqual(len(coms:=personaje.obtenerComandos(personaje)),5)
        print("..")
        print(coms)
        print(coms[0])
        coms[0].ejecutar(personaje)#Abrir armario 1
        coms= personaje.obtenerComandos(personaje)
        print(coms[0])
        coms[0].ejecutar(personaje)#Entrar en armario 1 
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Coger Pan
        self.assertEqual(len(mochila:=personaje.mochila.children),1)
        self.assertEqual((Pan:=mochila[0]).esPan(),True)
        self.assertEqual(len((coms:=Pan.obtenerComandos(personaje))),2)
        coms[0].ejecutar(personaje)#Soltar Pan
        self.assertEqual(Pan.padre,personaje.posicion)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Volver a coger Pan
        coms= personaje.mochila.children[0].obtenerComandos(personaje)
        print(coms)
        vida = personaje.corazones
        coms[1].ejecutar(personaje)#Comer Pan
        self.assertEqual(personaje.corazones, vida + Pan.vida) #Se le sumará la vida del Pan
        print(personaje.mochila.children)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Irse del armario
        coms= personaje.obtenerComandos(personaje)
        print(coms)
        bomba=coms[2].receiver
        corazones = personaje.corazones
        coms[2].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.corazones,corazones-bomba.damage)#Comprobamos que el personaje ha recibido daño de la explosión
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Abrimos la puerta 1 - 2
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Entramos en la habitación 2
        hab2 = self.juego.getHab(2)
        self.assertEqual(personaje.posicion,hab2)#Comprobamos que la posición del personaje es la habitación 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Cogemos la Katana...
        self.assertEqual(len(hijos:=personaje.mochila.children), 1)
        print(hijos)
        self.assertEqual((esc:=hijos[0]).esBatePinchos(),True)
        self.assertEqual(len(coms:=esc.commands),2)
        self.assertEqual(coms[0].esSoltar(),True)
        self.assertEqual(coms[1].esUsar(),True)
        bicho2 = self.juego.bichos[1]
        coms[1].ejecutar(personaje)
        self.assertEqual(personaje.posicion, bicho2.posicion) #Vemos si está en el mismo lugar que bicho perezoso.
        self.assertEqual(len(personaje.mochila.children),0)#Ya no tiene la Katana de metal en el inventario
        self.assertEqual(personaje.cuerpo.brazoAtaque,esc)#Tiene la Katana en la mano derecha
        print(bicho2.corazones)
        personaje.atacar()
        personaje.atacar()
        print(bicho2.corazones)
        self.assertEqual(bicho2.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la Katana.
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 4
        hab4 = self.juego.getHab(4)
        self.assertEqual(personaje.posicion,hab4)#Comprobamos que la posición del personaje es la habitación 4
        coms= personaje.obtenerComandos(personaje)
        bomba=coms[0].receiver
        corazones = personaje.corazones
        coms[0].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.corazones,corazones-bomba.damage)#Comprobamos que el personaje ha recibido daño de la explosión
        personaje.atacar()
        personaje.atacar()
        bicho4 = self.juego.bichos[3]
        self.assertEqual(bicho4.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la Katana.
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entramos en el armario 2
        self.assertEqual((arm:=personaje.posicion).esArmario(),True)
        self.assertEqual(arm.ref,2)#El armario es el armario 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Abandonamos el armario
        self.assertEqual(personaje.posicion,hab4)#La posición del personaje vuelve a ser la habitación 4
        coms= personaje.obtenerComandos(personaje)
        print("______________")
        print(coms)
        coms[2].ejecutar(personaje)
        print("###################")
        coms= personaje.obtenerComandos(personaje)
        print(coms)
        coms[2].ejecutar(personaje)#Entramos en la habitación 3
        hab3 = self.juego.getHab(3)
        self.assertEqual(personaje.posicion,hab3)#Comprobamos que la posición del personaje es la habitación 3
        personaje.atacar()
        personaje.atacar()
        personaje.atacar()
        self.assertEqual(self.juego.bichos[2].estaVivo(),False)#Matamos a un bicho agresivo con 3 golpes de Katana
        
        coms= personaje.obtenerComandos(personaje)
        print(coms[3], "Armario 3")
        coms[3].ejecutar(personaje)#Abrir armario 3
        coms= personaje.obtenerComandos(personaje)
        print(coms[3], "Armario 3")
        coms[3].ejecutar(personaje)#Entrar en armario 3 
        coms= personaje.obtenerComandos(personaje)
        print(coms[0])
        coms[0].ejecutar(personaje)#Coger Pocion
        self.assertEqual(len(mochila:=personaje.mochila.children),1)
        self.assertEqual((Pocion:=mochila[0]).esPocion(),True)
        self.assertEqual(len((coms:=Pocion.obtenerComandos(personaje))),2)
        print(coms[0])
        coms[0].ejecutar(personaje)#Soltar Pocion
        self.assertEqual(Pocion.padre,personaje.posicion)
        coms= personaje.obtenerComandos(personaje)
        print(coms[0])
        coms[0].ejecutar(personaje)#Volver a coger Pocion
        coms= personaje.mochila.children[0].obtenerComandos(personaje)
        vida = personaje.corazones
        print(vida)
        print(coms[1])
        coms[1].ejecutar(personaje)#Comer Pocion
        self.assertEqual(personaje.corazones, vida + Pocion.vida) #Se le sumará la vida de la Pocion
        print("Mochila --> ", personaje.mochila.children)
        coms= personaje.obtenerComandos(personaje)
        print(coms[1])
        coms[1].ejecutar(personaje)#Irse del armario
        coms= personaje.obtenerComandos(personaje)
        print(coms[4])
        coms[4].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        print(coms[4])
        coms[4].ejecutar(personaje)#Entramos en la habitación 1
        hab1 = self.juego.getHab(1)
        print(personaje.posicion)
        self.assertEqual(personaje.posicion,hab1)#Comprobamos que la posición del personaje es la habitación 1
        bichoFinal= self.juego.bichos[0]
        while bichoFinal.estaVivo():
            personaje.atacar()
        print("*******")
        self.assertEqual(self.juego.bichos[0].estaVivo(),False)
        self.juego.fase.esFinal()#El juego ha terminado al matar a los bichos.
        print("TEST FUNCIONALIDADES SUPERADO.\n")

if __name__ == '__main__':
    unittest.main()
