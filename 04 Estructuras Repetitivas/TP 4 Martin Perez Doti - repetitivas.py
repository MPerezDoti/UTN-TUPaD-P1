# Trabajo Práctico - Estructuras Repetitivas
# Tecnicatura Universitaria en Programación
# Autor: ChatGPT

# 1) Imprimir del 0 al 100 en orden creciente, un número por línea
print("1) Números del 0 al 100:")
for i in range(101):
    print(i)

# 2) Contar la cantidad de dígitos de un número entero
print("\n2) Cantidad de dígitos:")
num = int(input("Ingrese un número entero: "))
print(f"Cantidad de dígitos: {len(str(abs(num)))}")

# 3) Sumar todos los números entre dos valores (excluyéndolos)
print("\n3) Suma entre dos valores (excluidos):")
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print(f"La suma es: {suma}")

# 4) Sumar números hasta que el usuario ingrese un 0
print("\n4) Suma acumulada hasta ingresar 0:")
total = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print(f"Total acumulado: {total}")

# 5) Juego: adivinar un número del 0 al 9
import random
print("\n5) Adivina el número:")
secreto = random.randint(0, 9)
intentos = 0
while True:
    guess = int(input("Adivina el número (0-9): "))
    intentos += 1
    if guess == secreto:
        break
print(f"¡Correcto! Lo lograste en {intentos} intentos.")

# 6) Números pares entre 0 y 100 en orden decreciente
print("\n6) Números pares del 100 al 0:")
for i in range(100, -1, -2):
    print(i)

# 7) Suma desde 0 hasta un número ingresado
print("\n7) Suma de 0 hasta un número positivo:")
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print(f"La suma es: {suma}")

# 8) Ingresar 100 números y contar pares, impares, positivos y negativos
print("\n8) Contar pares, impares, positivos y negativos:")
pares = impares = positivos = negativos = 0
cantidad = int(input("¿Cuántos números desea ingresar? (hasta 100): "))
for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# 9) Calcular la media de 100 números
print("\n9) Media de N números:")
cantidad = int(input("¿Cuántos números desea ingresar? (hasta 100): "))
suma = 0
for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    suma += n
media = suma / cantidad
print(f"La media es: {media}")

# 10) Invertir los dígitos de un número
print("\n10) Invertir los dígitos de un número:")
num = input("Ingrese un número: ")
invertido = num[::-1]
print(f"Número invertido: {invertido}")
