from Forma.Forma import Forma

class Triangle(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.este = None
        self.oeste = None

    def esTriangulo(self):
        return True

    def __str__(self):
        return "\n   -Norte: " + str(self.norte) + "\n   -Este: " + str(self.este) + "\n   -Oeste: " + str(self.oeste)

    def __repr__(self):
        return self.__str__()
