class Partida():
	def puntuacion(self, ronda):
		rondas = [0,2,4,6,8,10,12,14,16,18,20]
		puntuacion = []
		puntos_extra = 0		
		for i in rondas:
			if i == 20:
				puntuacion.append(ronda[i])
			else:
				x = ronda[i] + ronda[i+1]
				if x <= 10:
					puntuacion.append(x)
		for i in range(0, len(puntuacion)):
			if puntuacion[i] == 10:
				if ronda[i*2] != 10:
					puntos_extra += ronda[(i+1)*2]
				else: 
					puntos_extra += puntuacion[i+1]

		return sum(puntuacion) + puntos_extra