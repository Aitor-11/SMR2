#factorial de los numeros que hay en la lista 
num = int(input("dime un numero : "))
factorial = 1
lista = []
for i in range(1, num + 1):
    factorial *= i
    lista.append(i)
print(f"El factorial de {num} es {factorial}")

'''
1. Solicitar al usuario que ingrese un número y almacenarlo en 'num'
2. Inicializar 'factorial' en 1 y crear una lista vacía
3. Repetir desde 1 hasta num: multiplicar factorial por cada número (i)
4. Agregar cada número a la lista
5. Mostrar el resultado del factorial de num '''