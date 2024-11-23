''''Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
llamadas a cada operador, y el total de las cuatro llamadas'''

tiempoLlamada11=float(input("Digite el tiempo de la primer llamada al operador 1: "))
tiempoLlamada12=float(input("Digite el tiempo de la segunda llamada al operador 1: "))
totalTiempo1= tiempoLlamada11 + tiempoLlamada12
costoOperador1=float(input("Digite el costo de la llamada al operador 1: "))
costoLlamada11=tiempoLlamada11*costoOperador1
costoLlamada12=tiempoLlamada12*costoOperador1
costoTotal1=costoOperador1*totalTiempo1
print(f"El costo de la primera llamada al operador 1 es: {costoLlamada11}")
print(f"El costo de la segunda llamada al operador 1 es: {costoLlamada12}")
print(f"El costo total de las llamadas al operador 1 es: {costoTotal1}")

tiempoLlamada21=float(input("Digite el tiempo de la primer llamada al operador 2: "))
tiempoLlamada22=float(input("Digite el tiempo de la segunda llamada al operador 2: "))
totalTiempo2= tiempoLlamada21 + tiempoLlamada22
costoOperador2=float(input("Digite el costo de la llamada al operador 2: "))
costoLlamada21=tiempoLlamada21*costoOperador2
costoLlamada22=tiempoLlamada22*costoOperador2
costoTotal2=costoOperador2*totalTiempo2
costoTotalOperador2 = costoTotal2 * totalTiempo2
costoTotalLlamadas = costoTotal1 + costoTotal2
print(f"El costo de la primera llamada al operador 2 es: {costoLlamada21}")
print(f"El costo de la segunda llamada al operador 2 es: {costoLlamada22}")
print(f"El costo total de las llamadas al operador 2 es: {costoTotal2}")
print(f"El Costo total de todas las llamadas es: {costoTotalLlamadas}")