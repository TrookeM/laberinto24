class Cuerpo():
    def __init__(self):
        self.brazoAtaque = None
        self.bodyObservers = []

    def addBodyObservers(self,obs):
        self.bodyObservers.append(obs)

    def obtenerArma(self):
        return self.brazoAtaque

    def setBatePinchos(self,obj):
        self.brazoAtaque = obj
        for obs in self.bodyObservers:
            obs.visualCuerpo()

    def obtenerComandos(self, ente):
        comandos = []
        if self.brazoAtaque is not None:
            comandos.extend(self.brazoAtaque.obtenerComandos(ente))
        return comandos
    
    def esCuerpo(self):
        return True