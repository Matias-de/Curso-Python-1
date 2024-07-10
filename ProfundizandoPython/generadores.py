#yield = producir
#funcion especial que retorna una secuencia de valores
#suspende la secuencia de la ejecucion de la funcion con la palabra yield (y no se usa return)

def generador():
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanuda la ejecucion')
    yield 3


#consumimos el generador a demanda

gen = generador()

#con cada llamada consumimos un valor

print(next(gen))
print(next(gen))
print(next(gen))
#si intentamos consumir más valores de los que produce el generador larga una excepcion
#print(next(gen))

#consumiendo los valores en un for

for valor in generador():
    print(f'Numero generado: {valor}')































































