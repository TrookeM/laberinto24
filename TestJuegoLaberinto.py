import unittest
from Juego import Juego

class TestJuego(unittest.TestCase):
    
    def test_createhabitacion_returns_habitacion_with_walls(self):
        juego = Juego()
        habitacion = juego.createhabitacion(1)
        self.assertIsNotNone(habitacion.norte)
        self.assertIsNotNone(habitacion.sur)
        self.assertIsNotNone(habitacion.este)
        self.assertIsNotNone(habitacion.oeste)

    def test_createhabitacion_returns_habitacion_with_correct_id(self):
        juego = Juego()
        habitacion = juego.construir_habitacion(5)
        self.assertEqual(habitacion.id, 5)
        
    def test_createhabitacion_returns_different_habitacions(self):
        juego = Juego()
        habitacion1 = juego.construir_habitacion(1)
        habitacion2 = juego.construir_habitacion(2)
        self.assertNotEqual(habitacion1, habitacion2)
