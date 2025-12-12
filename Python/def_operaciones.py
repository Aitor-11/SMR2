a = int(input("dame un numero : "))
b = int(input("dame otro numero: "))



def division(a, b):
    if a or b == 0 :
            return "ERROR 0 NO ES DIVISIBLE"
resultado = a / b


print("la division de los nuemros es ", division(a, b))
