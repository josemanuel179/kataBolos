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

	def test_partida_con_varios_strikes(self):
		partida = Partida()
		ronda = [(10,0),(8,1),(10,0),(4,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 52)

	def test_partida_con_varios_strikes_2(self):
		partida = Partida()
		ronda = [(10,0),(8,1),(6,3),(4,3),(1,1),(2,4),(10,0),(0,1),(7,0),(2,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 73)

	def test_partida_con_spare(self):
		partida = Partida()
		ronda = [(6,4),(5,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 22)

	def test_partida_con_spare(self):
		partida = Partida()
		ronda = [(6,4),(5,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 22)

	def test_partida_con_spare_y_puntos(self):
		partida = Partida()
		ronda = [(6,4),(5,2),(5,2),(6,1),(4,4),(4,2),(5,4),(1,1),(3,2),(2,2)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 70)

	def test_partida_con_varios_spares(self):
		partida = Partida()
		ronda = [(5,5),(3,2),(2,8),(6,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 42)











