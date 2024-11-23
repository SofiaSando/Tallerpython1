'''Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
referente al dinero que les corresponde en una herencia dejada por su esposo y padre
respectivamente. El testamento tiene las siguientes condiciones: A la esposa le corresponde el 40% mientras
que a los hijos les corresponde: 30% 20% 40% 10% respectivamente. Se pide un algoritmo
que lea los datos necesarios, y muestre lo que le corresponde a la esposa y a los hijos.'''

herenciaTotal = float(input("Digite el monto total de la herencia: "))
esposa = herenciaTotal * 0.40
restante=herenciaTotal-esposa
hijo1 = restante * 0.30
hijo2 = restante * 0.20
hijo3 = restante * 0.40
hijo4 = restante * 0.10
print(f"A la esposa le corresponde: {esposa}")
print(f"Al hijo 1 le corresponde: {hijo1}")
print(f"Al hijo 2 le corresponde: {hijo2}")
print(f"Al hijo 3 le corresponde: {hijo3}")
print(f"Al hijo 4 le corresponde: {hijo4}")
