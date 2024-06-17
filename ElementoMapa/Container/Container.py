import os
import sys

from ElementoMapa.ElementoMapa import ElementoMapa
import random

class Container (ElementoMapa):

    def __init__(self, n):
        super().__init__()
        self.ref = n
        self.objChildren = []
        self.form = None
        self.extent = None

    def recorrer(self, order):
        order(self)
        for ch in self.objChildren:
            ch.recorrer(order)
        self.form.recorrer(order)


    def estimarPosicion(self):
        self.form.estimarPosicion()

    def getPunto(self):
        return self.form.point
    
    def setPunto(self,punto):
        self.form.point = punto

    def getExtent(self):
        return self.form.alcance
    
    def setExtent(self, alc):
        self.form.alcance = alc

    def obtenerComandos(self, ente):
        
        juegoCommands=[]
        juegoCommands.extend(self.commands)

        for hijo in self.objChildren:
            juegoCommands.extend(hijo.obtenerComandos(ente))

        juegoCommands.extend(self.form.getCommands(ente))
        
        return juegoCommands

    def addChild(self, obj):
        obj.padre = self
        self.objChildren.append(obj)

    def putElementOn(self, obj1, obj2):
        self.form.putElementOn(obj1, obj2)
    
    def notifySubs(self):
        pass

    def addOr(self, orientacion):
        self.form.addOr(orientacion)

    def getRandOri(self):
        reference = random.randint(0,len(self.form.orientaciones)-1)
        return self.form.orientaciones[reference]

    def getChildren(self):
        return self.objChildren