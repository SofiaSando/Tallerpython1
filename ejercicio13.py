'''El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
para otros proyectos.'''

terrenoTotal = float(input("Digite el área total del terreno en metros cuadrados: "))
areaCultivos = terrenoTotal * 0.40
areaVivienda = terrenoTotal * 0.25
areaZonasVerdes = terrenoTotal * 0.15
areaDisponible = terrenoTotal - (areaCultivos + areaVivienda + areaZonasVerdes)

print(f"Área para cultivos: {areaCultivos} metros cuadrados.")
print(f"Área para vivienda: {areaVivienda} metros cuadrados.")
print(f"Área para zonas verdes: {areaZonasVerdes} metros cuadrados.")
print(f"Área disponible para otros proyectos: {areaDisponible} metros cuadrados.")
