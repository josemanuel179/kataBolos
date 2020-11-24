class Partida():
	def puntuacion(self, ronda):
		suma = 0
		for i in range(0, len(ronda)):
			suma += sum(ronda[i])
		return suma