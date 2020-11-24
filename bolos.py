class Partida():
	def puntuacion(self, ronda):
		suma = 0
		
		for i in range(0, len(ronda)):
			if ronda[i][0] == 10 and ronda[i][1] == 0:
				suma += sum(ronda[i]) + sum(ronda[i+1])
				continue
			elif ronda[i][0] != 10 and sum(ronda[i]) == 10:
				suma += sum(ronda[i]) + ronda[i+1][0]
				continue
			else:
				suma += sum(ronda[i])
				continue
		return suma