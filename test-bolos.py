import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):
	def test_dummy(self):
		partida = Partida()
		resultado = partida.dummy_method()
		self.assertEqual(resultado,0)