'''1. Diseña un programa que te pida tu edad e indique si eres mayor de edad
o no. Usa constantes para definir la edad que corresponde con la mayoría
de edad'''

edad = int(input("dime tu edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18 :
    print("Eres mayor de edad ")
else:
    print("Eres menor de edad")

print("Tu edad es:", edad)

'''2. Diseñar un programa que pida por teclado dos números enteros y un
menú que muestre las opciones de suma, resta, multiplicación, división y
el resto (módulo) de la división.'''

num1 = int(input("Dime un número entero: "))
num2 = int(input("Dime otro número entero: "))

print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")
print ("5. Resto (módulo)")



opcion = int(input("Elige una opción del menú (1-5):"))


if opcion == 1:
    print("La suma es:", num1 + num2)
elif opcion == 2:
    print("La resta es:", num1 - num2)
elif opcion == 3:
    print("la multiplicacion es:", num1 * num2)
elif opcion == 4:   
    if num2 !=0:
        print("La división es:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero.")
elif opcion == 5:
    if num2 != 0:
        print("El resto (módulo) es:", num1 % num2)
    else:
        print("Error: No se puede calcular el módulo con divisor cero.")
else:
    print("Opción no válida.")
    
    
''' 3. Programa que lee dos números y muestra el mayor en pantalla. Si son
iguales deberá mostrar un mensaje indicándolo.'''   

Num1 = int(input("dime un numero jefe: "))    
Num2 = int(input("dime otro numero jefe: "))    

if Num1 > Num2 :
    print("el primer numero  es mayor al segundo")
elif Num1 == Num2 :
    print("los numeros son iguales")
elif Num1 < Num2 :
    print("el segundo numero es mayor al primero")
#opcion facil 


Num1 = int(input("dime un numero jefe: "))    
Num2 = int(input("dime otro numero jefe: "))    

if Num1 > Num2 :
    print(f"el {Num1} es mayor al {Num2}")
elif Num1 == Num2 :
    print("los numeros son iguales")
elif Num1 < Num2 :
    print(f"el {Num2} es mayor al {Num1}")

#opcion con f


'''4. Programa que lea 3 números y que los imprima ordenados de mayor a
menor'''

opc1 = int(input("dime un numero: "))
opc2 = int(input("dime un numero: "))
opc3 = int(input("dime un numero: "))

numeros = [opc1,opc2,opc3]
numeros.sort(reverse=True)

print("y asi ordenados de mayor a menor")
print(",".join(str(n) for n in numeros))#opcion con listas y sort

