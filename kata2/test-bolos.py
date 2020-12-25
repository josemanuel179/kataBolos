import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_ronda_sin_puntos(self):
		partida = Partida()
		puntuacion = partida.prueba([0,0,0,0,0,0,0,0,0,0])
		self.assertEqual(puntuacion, 0)

	def test_ronda_con_un_punto(self):
		partida = Partida()
		puntuacion = partida.prueba([1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(puntuacion, 1)

	def test_romda_con_varios_puntos(self):
		partida = Partida()
		puntuacion = partida.prueba([1,2,3,4,5,0,0,0,0,0])
		self.assertEqual(puntuacion, 15)