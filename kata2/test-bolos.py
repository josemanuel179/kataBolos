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

	def test_ronda_con_varios_puntos(self):
		partida = Partida()
		puntuacion = partida.prueba([1,2,3,4,5,0,0,0,0,0])
		self.assertEqual(puntuacion, 15)

	def test_ronda_con_strike(self):
		partida = Partida()
		puntuacion = partida.prueba([10,0,0,0,0,0,0,0,0,0])
		self.assertEqual(puntuacion, 10)

	def test_ronda_con_strike_y_punto(self):
		partida = Partida()
		puntuacion = partida.prueba([10,3,0,0,0,0,0,0,0,0])
		self.assertEqual(puntuacion, 16)

	def test_ronda_strikes_y_puntos(self):
		partida = Partida()
		puntuacion = partida.prueba([10,3,5,0,10,10,4,0,0,0])
		self.assertEqual(puntuacion, 59)

	def test_con_ronda_extra(self):
		partida = Partida()
		puntuacion = partida.prueba([0,0,0,0,0,0,0,0,0,10,8])
		self.assertEqual(puntuacion, 59)

