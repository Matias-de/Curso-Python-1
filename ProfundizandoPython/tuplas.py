#tuplas

#declarar variable


a, b = 'Hola', 'Adios'
print(a, b)

# swap

a, b = b, a
print(a, b)

# regresar multiples valores en una funcion

def minMax(lista):
    return min(lista), max(lista)


min, max = minMax(list(range(1, 6)))
print(min, max)

#regresar la suma de una tupla

resultado = sum((1, 2, 3, 4, 5))
print(resultado)


def sumar(*args):
    return sum(args)


resultado = sumar(1, 2, 3, 4, 5)
print(resultado)









































