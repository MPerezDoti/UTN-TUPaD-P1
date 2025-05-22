# TP 5 - Listas - UTN a distancia

# 1) Crear lista con numeros del 1 al 100 multiplos de 4
lista_multiplos_4 = list(range(4, 101, 4))
print("1)", lista_multiplos_4)

# 2) Crear lista con 5 elementos y mostrar el penultimo
gustos = ["pizza", "musica", "cine", "futbol", "helado"]
print("2)", gustos[-2])

# 3) Crear lista vacia, agregar tres palabras con append e imprimirla
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3)", lista_vacia)

# 4) Reemplazar segundo y ultimo valor en lista animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4)", animales)

# 5)  Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print ("7) El programa en cuestion genera una lista llamada numeros compuesta por 5 numeros distintos, luego elimina el mas grande de ellos y printea la lista.")


# 6) Lista del 10 al 30 saltando de 5 en 5, mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("6)", numeros[:2])

# 7) Reemplazar los dos valores centrales en la lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiat", "renault"]
print("7)", autos)

# 8) Crear lista vacia y agregar el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8)", dobles)

# 9) Lista de compras por cliente - varias modificaciones
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("9)", compras)

# 10) Crear lista anidada segun especificacion
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10)", lista_anidada)
