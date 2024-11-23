'''Un atleta tiene la costumbre de medir el tiempo(en minutos) y la distancia (en metros)
durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
tiempo que duro el entrenamiento , la distancia recorrida, y el promedio del tiempo.'''

tiempoTotal = 0
distanciaTotal = 0

for dia in range(1, 4):
    tiempo = float(input(f"Digite el tiempo (en minutos) del día {dia}: "))
    distancia = float(input(f"Digite la distancia (en metros) del día {dia}: "))
    tiempoTotal += tiempo
    distanciaTotal += distancia

promedioTiempo = tiempoTotal / 3
promedioDistancia = distanciaTotal / 3

print(f"Total de tiempo de entrenamiento: {tiempoTotal} minutos.")
print(f"Total de distancia recorrida: {distanciaTotal} metros.")
print(f"Promedio de tiempo por día: {promedioTiempo} minutos.")
print(f"Promedio de distancia por día: {promedioDistancia} metros.")
