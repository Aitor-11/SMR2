''' Contador ascendente:
Escribe un programa que pida un número entero positivo y, usando un ciclo while, muestre todos los números desde 1 hasta ese número.'''

numero = int(input("dime un numero: "))
contador = 0

while contador < numero:
    contador += 1
    print(contador)


'''Suma hasta cero:
Pide números enteros al usuario de forma repetida. Usa un while para seguir pidiendo números hasta que el usuario ingrese un 0. 
Cuando termine, muestra la suma total de los números ingresados.'''

lista = []
while True :
    num = int(input("dime un numero: "))
    lista.append(num)
    lista_sumada = sum(lista)
    if num == 0:
        break
    else:
        continue
print("la suma total es: ", lista_sumada)


'''Adivinar el número:
Genera un número secreto entre 1 y 20. Luego, usando un while, pide al usuario que adivine el número hasta que acierte. 
Indica si el número ingresado es mayor o menor que el secreto.'''

import random
numero_secreto = random.randint(1,20)
while True:
    numero_usuario = int(input("Adivina el numero entre 1 y 20: "))
    if numero_usuario < numero_secreto:
        print("El numero es mayor")
    elif numero_usuario < 1 :
        print("Por favor ingresa un numero valido")
    elif numero_usuario > numero_secreto:
        print("El numero es menor")
    else:
        print("Felicidades, has adivinado el numero!")
        break
    



'''Contador de dígitos:'''


num = int(input("Ingresa un número entero: "))

contador = 0
n = abs(num)  # valor absoluto para evitar problemas con negativos

while n > 0:
    n //= 10
    contador += 1

print("El número tiene", contador, "dígitos.")
