"""Trabajo practico N° 1 para Programacion 1 en TUPaD"""

"""Martin Perez Doti"""

"""Actividades"""
""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""
print ("hola mundo")

""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
realizar la impresión por pantalla. """
nombre = input('ingrese su nombre \n')
print("Buenos dias ", nombre ,"!")

""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
la impresión por pantalla. """
nombre = input('ingrese su nombre \n')
apellido = input('ingrese su apellido \n')
edad = input('ingrese su edad (en años) \n')
residencia = input('ingrese su lugar de residencia \n')
print("Hola, soy", nombre , apellido, "tengo", edad, "años y vivo en", residencia, ", un gusto. \n")

""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro. """
radio = float(input('ingrese el radio del circulo para calcular su area y perimetro. \n'))
perimetro = radio * 3.14159 * 2
area = radio * radio * 3.14159
print("El circulo de radio", radio, "tendra un perimetro de", perimetro, "y un area de", area)

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """
segundos = int(input('ingrese la cantidad de segundos para calcular su equivalente en horas \n'))
horas = segundos / 3600.00
print(segundos, "segundos equivale a", horas, "horas \n")

""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número. """
numero = int(input('ingrese un numero para mostrar su tabla de multiplicar \n'))
for x in range (1, 11):
    resultado = numero * x
    print(numero, "multiplicado por", x, "es igual a", resultado, ". \n")

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """
numero1 = float(input('ingrese el primer numero \n'))
numero2 = float(input('ingrese el segundo numero \n'))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("la suma es igual a", suma, "\n", "la resta es igual a", resta, "\n", "la multiplicacion es igual a", multiplicacion, "\n", "la division es igual a", division, "\n")

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
IMC=pesoEnKg / (alturaEnMetros)alcuadrado """
altura = float(input('ingrese su altura en metros \n'))
peso = float(input('ingrese su peso en kg \n'))
imc= peso / (altura ** 2)

print("teniendo un peso de", peso, "y una altura de",altura, "el indice de masa corporal es de", imc, "\n")



""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

Temperatura en Fahrenheit = 9/5 . Temperatura en Celsius + 32 """
celcius = float(input('ingrese la temperatura en grados Celcius para convertir a Fahrenheit \n'))
fahrenheit= celcius * (9/5) + 32

print("un temperatura de", celcius, "equivale a ",fahrenheit,"\n")


""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """
numero1 = float(input("ingrese el primer numero para promediar\n"))
numero2 = float(input("ingrese el segundo numero para promediar\n"))
numero3 = float(input("ingrese el tercer numero para promediar\n"))
promedio = (numero1 + numero2 + numero3) / 3
print("el promedio de", numero1, ",", numero2, "y",numero3, "es igual a",promedio,"\n")
