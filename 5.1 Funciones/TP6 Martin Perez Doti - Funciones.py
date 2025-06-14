# tp funciones - programacion i
# tecnicatura universitaria en programacion
# Martin Perez Doti
# DNI 43150956

# 1. crear una funcion llamada imprimir_hola_mundo que imprima por pantalla el mensaje: "hola mundo!". llamar a esta funcion desde el programa principal.
def imprimirHolaMundo():
    print("hola mundo!")

imprimirHolaMundo()

# 2. crear una funcion llamada saludar_usuario(nombre) que reciba como parametro un nombre y devuelva un saludo personalizado. llamar a esta funcion desde el programa principal solicitando el nombre al usuario.
def saludarUsuario(nombre):
    return "hola " + nombre + "!"

nombre = input("ingresa tu nombre: ")
print(saludarUsuario(nombre))

# 3. crear una funcion llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parametros e imprima un mensaje personalizado. pedir los datos al usuario y llamar a la funcion con los valores ingresados.
def informacionPersonal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = input("ingresa tu edad: ")
residencia = input("ingresa tu lugar de residencia: ")
informacionPersonal(nombre, apellido, edad, residencia)

# 4. crear dos funciones: calcular_area_circulo(radio) y calcular_perimetro_circulo(radio). solicitar el radio al usuario y mostrar los resultados.
import math

def calcularAreaCirculo(radio):
    return math.pi * radio ** 2

def calcularPerimetroCirculo(radio):
    return 2 * math.pi * radio

radio = float(input("ingresa el radio del circulo: "))
print("area:", calcularAreaCirculo(radio))
print("perimetro:", calcularPerimetroCirculo(radio))

# 5. crear una funcion llamada segundos_a_horas(segundos) que devuelva la cantidad de horas correspondientes. solicitar al usuario los segundos.
def segundosAHoras(segundos):
    return segundos / 3600

segundos = int(input("ingresa la cantidad de segundos: "))
print("horas:", segundosAHoras(segundos))

# 6. crear una funcion llamada tabla_multiplicar(numero) que imprima la tabla de multiplicar del numero del 1 al 10.
def tablaMultiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("ingresa un numero para ver su tabla de multiplicar: "))
tablaMultiplicar(numero)

# 7. crear una funcion llamada operaciones_basicas(a, b) que devuelva una tupla con suma, resta, multiplicacion y division. mostrar los resultados.
def operacionesBasicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "division por cero")

a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))
resultados = operacionesBasicas(a, b)
print("suma:", resultados[0])
print("resta:", resultados[1])
print("multiplicacion:", resultados[2])
print("division:", resultados[3])

# 8. crear una funcion llamada calcular_imc(peso, altura) que devuelva el imc. solicitar al usuario los datos y mostrar el resultado con dos decimales.
def calcularImc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("ingresa tu peso en kg: "))
altura = float(input("ingresa tu altura en metros: "))
imc = calcularImc(peso, altura)
print(f"tu imc es: {imc:.2f}")

# 9. crear una funcion llamada celsius_a_fahrenheit(celsius) que devuelva su equivalente en fahrenheit. pedir al usuario la temperatura en celsius.
def celsiusAFahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("ingresa la temperatura en celsius: "))
print("temperatura en fahrenheit:", celsiusAFahrenheit(celsius))

# 10. crear una funcion llamada calcular_promedio(a, b, c) que devuelva el promedio de ellos. solicitar los numeros y mostrar el resultado.
def calcularPromedio(a, b, c):
    return (a + b + c) / 3

a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))
c = float(input("ingresa el tercer numero: "))
print("promedio:", calcularPromedio(a, b, c))
