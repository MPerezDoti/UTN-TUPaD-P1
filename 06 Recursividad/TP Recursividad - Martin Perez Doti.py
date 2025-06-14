#Resolución del Práctico 11: Aplicación de la Recursividad
#Martin Perez Doti
#DNI 43150956
# UTN - TUPaD - Programacion I

#1) Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("ingresa un numero: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")



#2) Serie de Fibonacci hasta cierta posición
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese una posición: "))
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")



#3) Potencia de un número (base^exponente)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input("base: "))
e = int(input("exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")



#4) Conversión de número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Número decimal: "))
binario = decimal_a_binario(num)
print("Binario:", binario if binario else "0")



#5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

p = input("Ingrese una palabra: ")
print("¿Es palíndromo?", es_palindromo(p))



#6) Suma de los dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

n = int(input("Número: "))
print("Suma de dígitos:", suma_digitos(n))



#7) Total de bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques:", contar_bloques(niveles))



#8) Contar cuántas veces aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Número: "))
d = int(input("Dígito a contar: "))
print("Cantidad de veces:", contar_digito(num, d))
