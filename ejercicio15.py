'''El sistema de liquidación que hacen los conductores de buses y los colectivos a las
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
al terminarlo . La diferencia de estos dos números determina el numero de pasajeros
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes
del dinero mientras el conductor recibe el resto.'''

inicioDia = int(input("Digite el número de la registradora al iniciar el día: "))
finDia = int(input("Digite el número de la registradora al finalizar el día: "))
valorPasaje = float(input("Digite el valor del pasaje: "))

totalPasajeros = finDia - inicioDia
totalRecaudado = totalPasajeros * valorPasaje

liquidadoConductor = totalRecaudado * 0.25
liquidadoEmpresa = totalRecaudado * 0.75

print(f"Total de pasajeros transportados: {totalPasajeros}")
print(f"Valor liquidado al conductor: {liquidadoConductor}")
print(f"Total liquidado a la empresa: {liquidadoEmpresa}")
