# Martin Ignacio Perez Doti
# DNI 43150956
# TUPaD – UTN FRSN



# TP 3 - Estructuras Condicionales
# Actividad 1
edad = float(input('Ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad')




# Actividad 2
nota = int(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')




# Actividad 3
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')




# Actividad 4
edad = int(input('Ingrese su edad: '))
if edad <= 12:
    print('Niño/a')
elif edad <= 18:
    print('Adolescente')
elif edad <= 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')




# Actividad 5
contrasena = input('Ingrese una contraseña: ')
if 8 <= len(contrasena) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')




# Actividad 6
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana > moda:
    print('Sesgo positivo')
elif media < mediana < moda:
    print('Sesgo negativo')
elif media == mediana == moda:
    print('Sin sesgo')
else:
    print('No se puede determinar el sesgo')




# Actividad 7
frase = input('Ingrese una frase o palabra: ')
if frase[-1].lower() in 'aeiou':
    frase += '!'
print(frase)




# Actividad 8
nombre = input('Ingrese su nombre: ')
opcion = int(input('Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para capitalizar: '))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())




# Actividad 9
magnitud = float(input('Ingrese la magnitud del terremoto: '))
if magnitud < 3:
    print('Muy leve')
elif magnitud < 4:
    print('Leve')
elif magnitud < 5:
    print('Moderado')
elif magnitud < 6:
    print('Fuerte')
elif magnitud < 7:
    print('Muy Fuerte')
else:
    print('Extremo')




# Actividad 10
hemisferio = input('Ingrese el hemisferio (N/S): ').upper()
mes = int(input('Ingrese el número del mes (1-12): '))
dia = int(input('Ingrese el día del mes: '))
fecha = (mes, dia)
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = 'Invierno'
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = 'Primavera'
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = 'Verano'
    else:
        estacion = 'Otoño'
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = 'Verano'
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = 'Otoño'
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = 'Invierno'
    else:
        estacion = 'Primavera'
else:
    estacion = 'Hemisferio inválido'
print('Estación:', estacion)
