import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_ronda_sin_puntos(self):
		partida = Partida()
		puntuacion = partida.prueba([0,0,0,0,0,0,0,0,0,0])
		self.assertEqual(puntuacion, 0)