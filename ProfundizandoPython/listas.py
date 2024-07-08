#profundizando listas
#listas = mutables

nombres = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()
#sumar listas
print(f'Sumar listas: {nombres + nombres2}')
#extender una lista con otra

nombres.extend(nombres2)
print(f' Extender la lista 1 con la lista 2: {nombres}')

#lista de numeros
numeros1 = [10, 40, 15, 4, 20, 90, 4]

#retornar indice del primer elemento encontrado
print(f'Lista original: {numeros1}')
print(f'Indice del elemento 4: {numeros1.index(4)}')
#invertir el orden de los elementos
numeros1.reverse()
print(f'Lista invertida: {numeros1}')
#ordenar por seleccion (ascendente)
numeros1.sort()
print(f'Lista ordenada: {numeros1}')
#ordenar de manera descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada descendente: {numeros1}')

#obtener el valor minimo y maximo
print(f'Valor minimo: {min(numeros1)}')

print(f'Valor maximo: {max(numeros1)}')

#copiar los elementos de una lista
numeros2 = numeros1.copy()
print(numeros1)
print(numeros2)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#usar constructor de la lista

numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#multiplicacion listas

listasMultiplicacion = 5*[[2, 5]]
print(listasMultiplicacion)
print(f'Misma referencia?: {listasMultiplicacion[0] is listasMultiplicacion[1]}')
print(f'Mismo contenido? {listasMultiplicacion[0] == listasMultiplicacion[1]}')
listasMultiplicacion[2].append(10)
print(listasMultiplicacion)

#matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Fila 0, columna 0: {matriz[0][0]}')
print(f'Fila 2, columna 2: {matriz[2][2]}')
print(f'Fila 2, columna 3: {matriz[2][3]}')
matriz[2][0] = 50
print(f'Matriz modificada: {matriz}')

listaListas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
listaListas.sort(key= len)
print(f'Ordenar lista: {listaListas}')

# sorted - built-in

nombres1 = ['Juan Carlos', 'Carla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)

#ordenar de manera descendente

nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

#ordenar por cantidad de caracteres
nombres1 = sorted(nombres1, key= len)
print(nombres1)

#built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))

