import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_dummy(self):
		partida = Partida()
		puntuacion = partida.puntuacion()
		self.assertEqual(puntuacion, 0)