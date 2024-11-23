'''Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%,
y posteriormente, le fue adicionado un 50% con relación al área después de la reducción.'''

terreno=float(input("Digite el area del terreno: "))
reducido=terreno*0.10
terrenoReducido=terreno-reducido
adicion=terrenoReducido*0.50
areaTotal=(terrenoReducido+adicion)
print(f"El area total del terreno es: {areaTotal}")