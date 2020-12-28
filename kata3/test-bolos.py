import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_ronda_sin_puntos(self):
		partida = Partida()
		ronda = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		puntuacion = partida.puntuacion(ronda)
		self.assertEqual(puntuacion, 0)

	def test_ronda_con_puntos(self):
		partida = Partida()
		ronda = [1,3,2,4,0,4,0,4,0,0,0,2,0,2,0,0,6,0,0,8,0]
		puntuacion = partida.puntuacion(ronda)
		self.assertEqual(puntuacion, 36)

	def test_ronda_con_strike_y_puntos(self):
		partida = Partida()
		ronda = [10,0,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		puntuacion = partida.puntuacion(ronda)
		self.assertEqual(puntuacion, 26)