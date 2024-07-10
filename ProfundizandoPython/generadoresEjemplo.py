#generador de numeros del 1 al 5

def generadorNumeros():
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejecucion')


#utilizamos el generador

generador = generadorNumeros()
print(f'Objeto generador: {generador}')

#consumir los valores del generador

for valor in generador:
    print(f'Numero producido: {valor}')

#consumir a demanda

generador = generadorNumeros()
try:
    print(f'consumir a demanda: {next(generador)}')
    print(f'consumir a demanda: {next(generador)}')
    print(f'consumir a demanda: {next(generador)}')
    print(f'consumir a demanda: {next(generador)}')
    print(f'consumir a demanda: {next(generador)}')
    print(f'consumir a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error a consumir generador: {e}')

#otra forma de consumir

generador = generadorNumeros()
op = True
while op:
    try:
        valor = next(generador)
        print(f'Valor generado desde while: {valor}')
    except StopIteration as e:
        print(f'Se termino de iterar el generador')
        op = False







