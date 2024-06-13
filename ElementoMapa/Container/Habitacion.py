from ElementoMapa.Container.Container import Container
from ElementoMapa.ElementoMapa import ElementoMapa
class Habitacion(Container):

    def entrar(self, obj):
        obj.setPosicion(self)
        print("Se encuentra ahora en la habitacion",self.ref)
    
    def aceptar(self, vst):
        print("Visitar habitación ", str(self.num))
        vst.visitarHabitacion(self)
        for ch in self.objChildren:
            ch.aceptar(vst)
        self.form.aceptar(vst)

    def esHabitacion(self):
        return True
    
    def __str__(self):
        info= "En la habitacion " + str(self.ref) +" tenemos estos elementos:" + str(self.form) 
        
        if len(self.objChildren)>0:
            dt = info + "\n [DETALLE DE LOS HIJOS]:"
            for n in self.objChildren:
                dt = dt + "\n["+str(n)+"]"
        return dt