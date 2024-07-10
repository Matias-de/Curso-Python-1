numeros = range(10)
listaPares = []

#creamos una nueva lista con los valores pares multiplicados por si mismo

for numero in numeros:
    #revisamos si es par
    if numero % 2 == 0:
        listaPares.append(numero*numero)


print(f'Lista pares: {listaPares}')

#hacemos lo mismo pero con list comprehensions
#expresion for var in coleccion if condicion (opcional)

listaPares = []

listaPares = [numero * numero for numero in numeros if numero % 2 == 0]

print(f'Lista pares con list comprehensions: {listaPares}')

#solo se agrega a la lista si el numero es divisible entre 2 y 6

pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(f'Lista dividibles por 2 y 6: {pares}')

#agregando if else
listaPares = []
listaImpares = []
for numero in range(10):
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

print(f'Lista pares: {listaPares}')
print(f'Lista Impares: {listaImpares}')

listaPares = []
listaImpares = []
[listaPares.append(numero) if numero % 2 == 0 else listaImpares.append(numero) for numero in range(10)]
print(f'Lista pares: {listaPares}')
print(f'Lista Impares: {listaImpares}')

#lista de lista
listaDeListas = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

listaSimple = [valor for sublista in listaDeListas for valor in sublista]
print(f'Lista simple: {listaSimple}')

#lista de numeros pares a partir de la lista de listas

listaPares = [valor for sublista in listaDeListas for valor in sublista if valor % 2 == 0]
print(listaPares)






