import random

# Elemento del Mapa
class ElementoMapa:
  def __init__(self):
    pass

  def entrar(self, alguien):  # Changed "someone" to "alguien" for consistency
    pass

  def imprimir(self):
    print("ElementoMapa")

  def esHabitacion(self):
    return False

class Contenedor(ElementoMapa):
  # Composite
  def __init__(self):
    super().__init__()
    self.hijos = []  # Changed "children" to "hijos" (children in Spanish)
    self.orientaciones = []

  def agregar_componente(self, componente):
    self.hijos.append(componente)

  def remover_componente(self, componente):
    self.hijos.remove(componente)

  def imprimir(self):
    print("Contenedor")

  def caminar_aleatorio(self, alguien):  # Introduced "caminar_aleatorio" for walkRandom
    pass

  def agregar_orientacion(self, orientacion):
    self.orientaciones.append(orientacion)

  def remover_orientacion(self, orientacion):
    self.orientaciones.remove(orientacion)

  def caminar_aleatorio(self, alguien):
    orientacion = self.obtener_orientacion_aleatoria()
    orientacion.caminar_aleatorio(alguien)

  def obtener_orientacion_aleatoria(self):
    return random.choice(self.orientaciones)

  def ir_al_norte(self, alguien):
    self.norte.entrar(alguien)

  def ir_al_este(self, alguien):
    self.este.entrar(alguien)

  def ir_al_sur(self, alguien):
    self.sur.entrar(alguien)

  def ir_al_oeste(self, alguien):
    self.oeste.entrar(alguien)

  def establecer_elemento_y_orientacion(self, elemento, orientacion):
    orientacion.establecer_elemento_y_orientacion(elemento, self)

class Laberinto(Contenedor):
  def __init__(self):
    super().__init__()

  def agregar_habitacion(self, habitacion):
    self.agregar_componente(habitacion)

  def entrar(self, alguien):
    self.hijos[0].entrar(alguien)

  def imprimir(self):
    print("Laberinto")

  def obtener_habitacion(self, id):
    for habitacion in self.hijos:
      if habitacion.id == id:
        return habitacion
    return None

class Habitacion(Contenedor):
  def __init__(self, id_habitacion):
    super().__init__()
    self.id = id_habitacion
    self.norte = None
    self.sur = None
    self.este = None
    self.oeste = None

  def entrar(self, alguien):
    print(alguien + " entra a la habitación", self.id)

  def imprimir(self):
    print("Habitación")

  def esHabitacion(self):
    return True

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
  def __init__(self):
    super().__init__()
    self.activa = False

  def imprimir(self):
    print("Bomba")

  def entrar(self, alguien):
    print(alguien + " pisó una bomba")

# Laberinto (modificado ligeramente)
class Laberinto(Contenedor):
  def __init__(self):
    self.habitaciones = []  # Changed "children" to "habitaciones" for clarity

  def agregar_habitacion(self, habitacion):
    self.habitaciones.append(habitacion)

  def entrar(self, alguien):
    self.habitaciones[0].entrar(alguien)

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

# Pared
class Pared(ElementoMapa):
    def __init__(self):
        pass

    def imprimir(self):
        print("Pared")

    def entrar(self, alguien):
        print(alguien, " chocó contra una pared")

# ParedBomba
class ParedConBombas(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def imprimir(self):
        print("Pared con Bombas")

    def entrar(self, alguien):
        print(alguien + " chocó contra una pared con bombas")
        if self.activa:
            print(alguien + " detonó una bomba")


# Puerta
class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self, alguien):
        if self.abierta:
            self.lado2.entrar(alguien)
        else:
            print("La puerta está cerrada")

    def imprimir(self):
        print("Puerta")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

class Orientación:
  def __init__(self):
    pass

  def caminar_aleatorio(self, alguien):
    pass

  def establecer_elemento_y_orientacion(self, em, aContainer):
    pass

class Norte(Orientación):
  _instance = None
  def __init__(self):
    if not Norte._instance:
      super().__init__()
      Norte._instance = self

  def setEMinOr(self, em, aContainer):
    aContainer.norte = em

  @classmethod
  def get_instance(cls):
    if not cls._instance:
      cls._instance = Norte()
    return cls._instance

  def print(self):
    print("Norte")

  def caminar_aleatorio(self, someone):
    someone.goNorth()

class Sur(Orientación):
  _instance = None
  def __init__(self):
    if not Sur._instance:
      super().__init__()
      Sur._instance = self

  @staticmethod
  def get_instance():
    if not Sur._instance:
      Sur()
    return Sur._instance

  def print(self):
    print("Sur")

  def caminar_aleatorio(self, someone):
    someone.goSouth()

  def setEMinOr(self, em, aContainer):
    aContainer.sur = em

class Este(Orientación):
  _instance = None
  def __init__(self):
    raise RuntimeError('Call instance() instead')

  @classmethod
  def get_instance(cls):
    if cls._instance is None:
      print('Creating new instance')
      cls._instance = cls.__new__(cls)
    return cls._instance

  def caminar_aleatorio(self, someone):
    someone.goEast()

  def setEMinOr(self, em, aContainer):
    aContainer.este = em

class Oeste(Orientación):
  _instance = None
  def __init__(self):
    if not Oeste._instance:
      super().__init__()
      Oeste._instance = self

  @staticmethod
  def get_instance():
    if not Oeste._instance:
      Oeste()
    return Oeste._instance

  def print(self):
    print("Oeste")

  def caminar_aleatorio(self, someone):
    someone.goWest()

  def setEMinOr(self, em, aContainer):
    aContainer.oeste = em

