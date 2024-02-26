# Elemento Mapa
class ElementoMapa:
    def __init__(self):
        pass
    
    def entrar(self):
        pass

    def imprimir(self):
        print("ElementoMapa")

class Contenedor(ElementoMapa):
    # Composite
    def __init__(self):
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def remover_componente(self, componente):
        self.componentes.remove(componente)
    
    def imprimir(self):
        print("Contenedor")

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregar_habitacion(self, habitacion):
        self.componentes.append(habitacion)

    def entrar(self):
        self.componentes[0].entrar()

    def imprimir(self):
        print("Laberinto")

class Habitacion(Contenedor):
    def __init__(self, id_habitacion):
        super().__init__()
        self.id = id_habitacion
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self):
        print("Has entrado a la habitación", self.id)
    
    def imprimir(self):
        print("Habitación")

class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("Hoja")

class Decorador(Hoja):
    def __init__(self):
        super().__init__()
        self.componente = None
    
    def imprimir(self):
        print("Decorador")

class Bomba(Decorador):
    pass

# Laberinto
class Laberinto(Contenedor):
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def entrar(self):
        self.habitaciones[0].entrar()
    
    def imprimir(self):
        print("Laberinto")

# Habitacion
class Habitacion(ElementoMapa):
    def __init__(self, id):
        self.id = id
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    
    def entrar(self):
        print("Has entrado a la habitación", self.id)

    def imprimir(self):
        print("Habitación")

# Pared
class Pared(ElementoMapa):
    def __init__(self):
        pass
    
    def imprimir(self):
        print("Pared")

# ParedBomba
class ParedConBombas(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
    
    def imprimir(self):
        print("ParedConBombas")

# Puerta
class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta está cerrada")

    def imprimir(self):
        print("Puerta")
