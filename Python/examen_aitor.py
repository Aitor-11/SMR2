# imprimir letras repetidas 
'''1. Crear una cadena de texto
2. Crear una lista vacía
3. Recorrer cada letra de la cadena
4. Si la letra no está en la lista, agregarla
5. Imprimir todas las letras únicas unidas sin separadores'''
texto = "programacion"
lista = []
for letra in texto:
    if letra not in lista:
        lista.append(letra)
print("".join(lista))

# letras repetidas 
'''1. Crear una cadena de texto
2. Crear una lista vacía para letras repetidas
3. Recorrer cada letra de la cadena
4. Si la letra ya está en repetidas, continuar (saltarla)
5. Si la letra aparece más de una vez en el texto, agregarla
6. Mostrar cuántas letras se repiten'''
texto = "programacion"
repetidas = []
for letra in texto:
    if letra in repetidas:
        continue
    if texto.count(letra) > 1:
        repetidas.append(letra)

print(f"se repiten {len(repetidas)} letras")


#cadena con las letras repetidas

'''1. Crear una cadena de texto
2. Crear una lista vacía para letras repetidas
3. Recorrer cada letra de la cadena
4. Si la letra ya está en repetidas, continuar (saltarla)
5. Si la letra aparece más de una vez, agregarla e imprimir en mayúscula'''
texto = "programacion"
repetidas = []
for letra in texto:
    if letra in repetidas:
        continue
    if texto.count(letra) > 1:
        repetidas.append(letra)
        print("".join(repetidas).upper())