from ElementoMapa.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def entrar(self,ente):
        print("Te has chocado")

    def aceptar(self,visitor):
        print("Has visitado una pared.")
        visitor.visitaPared(self)

    def EstimarDistancia(self):
        pass

    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"
    
    def __repr__(self):
        return "Pared"