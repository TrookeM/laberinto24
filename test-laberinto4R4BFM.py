import unittest
from Laberinto import Habitacion
from Juego import Juego

class TestJuego(unittest.TestCase):

    def test_crear4Habitaciones4BestiasFM(self):
        juego = Juego()
        juego.crear4Habitaciones4BestiasFM()
        
        # Verificar número de habitaciones
        self.assertEqual(len(juego.laberinto.hijos), 4)
        self.assertEqual(len(juego.bestias), 4)
        
        # Verificar conexiones entre habitaciones
        habitacion1 = juego.laberinto.obtenerHabitacion(1)
        habitacion2 = juego.laberinto.obtenerHabitacion(2) 
        habitacion3 = juego.laberinto.obtenerHabitacion(3)
        habitacion4 = juego.laberinto.obtenerHabitacion(4)

        
        self.assertIs(habitacion1.sur, habitacion2.norte)
        self.assertIs(habitacion1.este, habitacion3.oeste)
        self.assertIs(habitacion2.este, habitacion4.oeste)
        self.assertIs(habitacion3.sur, habitacion4.norte)
        
        # Verificar posiciones de las bestias
        self.assertTrue(juego.bestias[0].posicion.esHabitacion)
        self.assertTrue(juego.bestias[1].posicion.esHabitacion)
        self.assertTrue(juego.bestias[2].posicion.esHabitacion)
        self.assertTrue(juego.bestias[3].posicion.esHabitacion)
        
        self.assertIs(juego.bestias[0].posicion, habitacion1)
        self.assertIs(juego.bestias[1].posicion, habitacion2)
        self.assertIs(juego.bestias[2].posicion, habitacion3)
        self.assertIs(juego.bestias[3].posicion, habitacion4)
        
        self.assertTrue(juego.bestias[0].esAgresiva())
        self.assertTrue(juego.bestias[1].esPerezosa())
        self.assertTrue(juego.bestias[2].esAgresiva())
        self.assertTrue(juego.bestias[3].esPerezosa())

       
if __name__ == '__main__':
    unittest.main()
