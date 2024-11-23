'''El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
numero de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros
cuadrados.'''

alto = float(input("Digite el alto del muro en metros: "))
ancho = float(input("Digite el ancho del muro en metros: "))
areaBaño = alto * ancho
baldosasNecesarias = areaBaño / 3.5
print(f"El área del baño es: {areaBaño:.2f} metros cuadrados.")
print(f"El número de baldosas necesarias es: {baldosasNecesarias:.2f}")
