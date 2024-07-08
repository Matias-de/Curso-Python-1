#desempaquetar

numeros = [1, 2, 3]
print(*numeros)
print(*numeros, sep=' - ')

#desempaquetar al pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')


sumar(*numeros)

#extraer algunas partes de una lista

miLista = [1, 2, 3, 4, 5, 6]
a, *b, c, d = miLista
print(a, b, c, d)

#unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [*lista1, *lista2]
print(lista3)

#unir mapas

mapa1 = {'A': 1, 'B': 2, 'C': 3}
mapa2 = {'D':4, 'E': 5}
mapa3 = {**mapa1, **mapa2}
print(mapa3)
#construir una lista a partir de un str

lista = [*'holaMundo']
print(*lista, sep='')