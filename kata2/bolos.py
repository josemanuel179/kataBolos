class Partida():
	def prueba(self, ronda):
		puntos_extra = 0
		for i in range(0, len(ronda)-1):
			if ronda[i] == 10:
				puntos_extra += ronda[i+1]
		if ronda[9] == 10:
			puntos_extra += ronda[i+1]
		return sum(ronda) + puntos_extra

		if ronda[i] + ronda[i+1] == 10


	def partida(self, partida):
		rango = [0,2,4,6,8,10,12,14,16,18]
		resultado = 0
		puntos_extra = 0
		puntuacion = list()

		for i in rango:
			ronda = partida[i] + partida[i+1]
			puntuacion.append(ronda)

		for i in range(0, len(puntuacion)):
			if puntuacion[i] == 10:
				if partida[i*2] == 10:
					puntos_extra += puntuacion[i+1]
				else:
					puntos_extra += partida[(i+1)*2]

	resultado = sum(puntuacion) + puntos_extra
	return resultado