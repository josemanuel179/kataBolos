class Partida():
	def prueba(self, ronda):
		puntos_extra = 0
		for i in range(0, len(ronda)):
			if ronda[i] == 10:
				puntos_extra += ronda[i+1]
		return sum(ronda) + puntos_extra