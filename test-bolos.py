import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_partida_sin_puntos(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 0)
