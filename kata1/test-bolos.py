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

	def test_partida_con_varios_spares(self):
		partida = Partida()
		ronda = [(5,5),(3,2),(2,8),(6,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 42)

	def test_partida_con_varios_spares_y_puntos(self):
		partida = Partida()
		ronda = [(5,4),(3,4),(2,8),(5,0),(3,5),(8,2),(7,1),(2,2),(0,10),(3,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 89)

	def test_partida_con_varios_spares_y_puntos(self):
		partida = Partida()
		ronda = [(5,4),(3,4),(2,8),(5,0),(3,5),(8,2),(7,1),(2,2),(0,10),(3,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 89)

	def test_partida_con_bonus(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(10,0),(3,5)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 26)

	def test_partida_con_bonus_2(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(6,4),(3,5)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 21)

	def test_tirada_incorrecta(self):
		partida = Partida()
		ronda = [(10,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertFalse(puntuacion_total, 12)

	def test_tirada_spare_strike(self):
		partida = Partida()
		ronda = [(5,5),(10,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 30)

	def test_tirada_strike_spare(self):
		partida = Partida()
		ronda = [(10,0),(5,5),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 32)

	def test_partida_random_1(self):
		partida = Partida()
		ronda = [(6,3),(10,0),(5,3),(5,5),(2,8),(4,0),(1,1),(4,5),(2,3),(1,5)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 87)

	def test_partida_random_2(self):
		partida = Partida()
		ronda = [(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0),(10,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 210)

	def test_partida_random_3(self):
		partida = Partida()
		ronda = [(5,4),(2,4),(4,5),(6,4),(5,3),(2,2),(1,9),(6,0),(10,0),(5,0)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 93)

	def test_partida_random_4(self):
		partida = Partida()
		ronda = [(5,3),(7,1),(6,2),(10,0),(6,0),(5,1),(9,1),(4,2),(8,1),(5,2)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 88)

	def test_partida_random_5(self):
		partida = Partida()
		ronda = [(5,2),(3,5),(10,0),(6,2),(6,1),(9,1),(5,1),(10,0),(9,1),(7,1)]
		puntuacion_total = partida.puntuacion(ronda)
		self.assertEqual(puntuacion_total, 114)










