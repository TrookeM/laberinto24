class Forma():
    
    def __init__(self):
        self.ref = None
        self.point = None
        self.alcance = None
        self.orientaciones = []


    def addOr(self, ori):
        self.orientaciones.append(ori)
    
    def getCommands(self, obj):
        setComandos = []

        for o in self.orientaciones:
            setComandos.extend(o.getCommands(self, obj))

        return setComandos
    
    def estimarPosicion(self):
        for o in self.orientaciones:
            o.verPosicion(self)
    
    def accept(self,visitor):

        for o in self.orientaciones:
            o.accept(visitor, self)

    def getElement(self, ori):
        return ori.getElement(ori)
    
    def putElementOn(self, orientacion, elem):
        orientacion.putElementOn(elem, self)

    def recorrer(self, ref):
        for o in self.orientaciones:
            o.recorrerEn(self, ref)

    def esCuadrado(self):
        return False
    
    def esRombo(self):
        return False

    def esTriangulo(self):
        return False
