# bestia.py
class Bestia:
    def __init__(self, modo):
        self.modo = modo
        self.poder = 2
        self.vida = 10

# modo.py
class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def imprimir(self):
        print("Bestia Agresiva")

class Perezoso(Modo):
    def imprimir(self):
        print("Bestia Perezosa")