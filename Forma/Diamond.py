from Forma.Forma import Forma

class Diamond(Forma):

    def __init__(self):
        super().__init__()

        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None

    def esRombo(self):
        return True

    def __str__(self):
        return "\n   -Noreste: " + str(self.noreste) +"\n   -Noroeste: " + str(self.noroeste) +"\n   -Sureste: " + str(self.sureste) +"\n   -Suroeste: " + str(self.suroeste)
 