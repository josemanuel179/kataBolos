import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_ronda_sin_puntos(self):
		partida = Partida()
		ronda = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		puntuacion = partida.puntuacion(ronda)
		self.assertEqual(puntuacion, 0)