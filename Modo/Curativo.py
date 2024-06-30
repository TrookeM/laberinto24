from Modo.Modo import Modo

class Curativo(Modo):
    
    def atacar(self, unBicho):
        unBicho.actuar()
    
    def curar(self, unBicho):
        unBicho.set_corazones(unBicho.corazones + 50)  # Aquí se asegura que el Bicho se cure
        print(f"Lagartija curativa se ha curado y ahora tiene {unBicho.corazones} corazones.")  # Mensaje de curación

    
    def esCurativo(self):
        return True
    
    def __str__(self):
        return "Lagartija curativa aparecio"
