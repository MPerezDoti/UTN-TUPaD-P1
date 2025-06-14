# Martin Perez Doti
# DNI 43150956
# UTN - TUPaD - Programacion I


# 1) Dado el diccionario precios_frutas, agregar nuevas frutas con sus precios
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar los precios de Banana, Manzana y Melon
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

# 3) Crear una lista con solo las frutas (sin precios)
solo_frutas = list(precios_frutas.keys())

# 4) Agenda telefonica: cargar 5 contactos y consultar por nombre
agenda = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero de telefono: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre a consultar: ")
if consulta in agenda:
    print(f"Numero de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado")

# 5) Solicitar una frase e imprimir palabras unicas y ocurrencias
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)

frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Palabras unicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencias)

# 6) Ingresar nombres de 3 alumnos y sus 3 notas, mostrar promedios
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese nota {i+1}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# 7) Dado dos sets de estudiantes que aprobaron parcial 1 y 2, mostrar:
parcial1 = {"Ana", "Luis", "Juan", "Marta"}
parcial2 = {"Luis", "Marta", "Pedro", "Sofia"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Diccionario de stock: consultar, agregar unidades o productos
stock = {"arroz": 10, "azucar": 5}

producto = input("Ingrese producto a consultar: ")
if producto in stock:
    agregar = int(input("Cuantas unidades desea agregar?: "))
    stock[producto] += agregar
else:
    nuevo = int(input("Producto no encontrado. Ingrese cantidad para nuevo producto: "))
    stock[producto] = nuevo

print("Stock actualizado:", stock)

# 9) Agenda de eventos con clave (dia, hora) y valor evento
agenda_eventos = {
    ("lunes", "10:00"): "reunion",
    ("martes", "14:00"): "clase"
}

dia = input("Ingrese dia: ")
hora = input("Ingrese hora: ")
evento = agenda_eventos.get((dia, hora), "No hay eventos agendados")
print(f"Evento el {dia} a las {hora}: {evento}")

# 10) Invertir un diccionario pais:capital a capital:pais
paises = {"Argentina": "Buenos Aires", "Francia": "Paris", "Japon": "Tokyo"}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
