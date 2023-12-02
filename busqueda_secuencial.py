def busqueda_secuencial(lista, valor):
 
    posicion = 0
    encontrado = False


    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1

        return encontrado, posicion
    

numeros = [2, 7, 3, 5, 13, 31, 29, 17, 19] 
llave = 41
print(busqueda_secuencial(numeros, llave))

llave = 13
print(busqueda_secuencial(numeros, llave))

llave = 17
print(busqueda_secuencial(numeros, llave))



