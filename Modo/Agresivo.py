from Modo.Modo import Modo

class Agresivo(Modo):
    
    def atacar(self,unBicho):
        unBicho.actuar()
    
    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "Rata de cloaca apareció"
