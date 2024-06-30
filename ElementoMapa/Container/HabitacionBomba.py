from ElementoMapa.Container.Habitacion import Habitacion

class HabitacionBomba(Habitacion):

    def __init__(self, ref):
        super().__init__(ref)
        self.activa = True
        self.ref = ref

    def entrar(self):
        if self.activa:
            print("¡BOOOOOOOOOOM! La bomba ha explotado...")
            self.activa = False
        else:
            print("Entraste a la habitación [{#",self.ref, "#}] \n")