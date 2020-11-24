import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_partida_sin_puntos(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 0)

	def test_partida_con_un_punto(self):
		partida = Partida()
		ronda = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 1)

	def test_partida_con_varios_puntos(self):
		partida = Partida()
		ronda = [(5,0),(6,2),(8,0),(1,1),(6,3),(8,0),(9,0),(3,4),(4,4),(5,2)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 71)

	def test_partida_con_strike(self):
		partida = Partida()
		ronda = [(10,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 10)

	def test_partida_con_strike_y_puntos(self):
		partida = Partida()
		ronda = [(10,0),(0,0),(5,0),(6,0),(5,0),(0,1),(0,4),(0,0),(1,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 32)

	def test_partida_con_strike_y_puntos_2(self):
		partida = Partida()
		ronda = [(10,0),(4,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 22)

