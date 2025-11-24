'''1) Mete los valores del 1 al 100 en una lista.
a) Imprimirlos ordenados
b) Imprimirlos al revés.
c) Pide un número por teclado y comprueba si se encuentra en la lista. En caso de que si esté
debe salir del bucle.'''

lista = list(range(1, 100))
print(f"{lista} imprimida ordenada")

lista.sort(reverse=True)
print(f"{lista} imprimida al reves")

while True:
    num = int(input("dime un numero del 1 al 100: "))
    if num in lista:
        print(f"el numero {num} esta en la lista")
        break    
    else:
        print(f"el numero {num} no esta en la lista")
        continue
    

'''2) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo,
si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50'''

Num = int(input("dime un numero para sacar su tabla de multiplicar: "))
tabla = [Num * 1, Num * 2, Num * 3, Num * 4, Num * 5, Num * 6, Num * 7, Num * 8, Num * 9, Num * 10]
print(f"la tabla de multiplicar del {Num} es: {tabla}")


'''3) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de
los números'''
lista = []

i = 0
while i < 10:
    valor = int(input(f"dime el valor que hay que añadir a  la lista: "))
    i += 1
    lista.append(valor)
print(f"{lista}")

suma = sum(lista)
media = suma / len(lista)
print(f"La suma de los valores de la lista es: {suma}")
print(f"la media de la lista es : {media}")

'''4) Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero. (while)'''

meses = ("ERROR","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

while True:
    i = int(input("introduce un numero de un mes: "))
    if i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12):
        print(meses[i])
    else:
        print("ERROR")
        break
    
'''5) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por
último, muestra los números ordenados de menor a mayor.
Usa el método sort para ordenar'''
lista = []
while True:
    valor = int(input("dame una lista de numeros jefe"))
    if valor == 0:
        break
lista.append[valor]
lista.sort
print(f"ordenados de menor a mayor {lista}")
'''6) Lo mismo que el anterior pero ordenando de mayor a menor.'''
lista = []
while True:
    valor = int(input("dame una lista de numeros jefe"))
    if valor == 0:
        break
lista.append[valor]
print(f"ordenados de menor a mayor {lista}")


'''7) Pide una cadena por teclado, mete los caracteres en una lista sin espacios.'''
input_cadena = input("dime una cadena de texto: ")
lista_caracteres = []
for caracter in input_cadena:
    if caracter != " ":
        lista_caracteres.append(caracter)
print(f"Lista de caracteres sin espacios: {lista_caracteres}")

'''8) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.'''
input_cadena = input("dime una cadena de texto: ")
lista_caracteres = []
for caracter in input_cadena:
    if caracter not in lista_caracteres:
        lista_caracteres.append(caracter)
print(f"Lista de caracteres sin repetir: {lista_caracteres}")

'''9) Dada la siguiente tupla, pide un numero por teclado e indica cuantas veces se repite.
numeros = (5,4,3,2,1,6,45,3,6,6,6,6,6)'''
numeros = (5,4,3,2,1,6,45,3,6,6,6,6,6)
num = int(input("dime un numero: "))
print(f"El numero {num} se repite {numeros.count(num)} veces.")

'''10) Dada la siguiente tupla indica el numero con mayor valor y el que menor tenga.
numeros = (5,4,3,-2,1,6,455,3,6,6,6,6,6)'''
numeros = (5,4,3,-2,1,6,455,3,6,6,6,6,6)
print(f"El numero mayor es: {max(numeros)}")
print(f"El numero menor es: {min(numeros)}")