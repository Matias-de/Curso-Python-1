#funciones pequeñas y anonimas

def sumar(a, b):
    return a + b


#con una funcion lambda (anonima, sin nombre y una sola linea de codigo
#no se necesitan parentesis
#return no necesario, pero si debe regresar una expresion valida

miFuncionLambda = lambda a, b: a + b

resultado = miFuncionLambda(10, 5)
print(f'Resultado de sumar con funcion lambda: {resultado}')

#funcion lambda que no recibe argumentos (si se debe retorenar una expresion valida)

miFuncionLambda = lambda: 'Funcion sin argumentos'

print(f'Llamar funcion lambda sin argumentos: {miFuncionLambda()}')

#funcion lambda con parametros por default

miFuncionLambda = lambda a=2, b=3: a + b
print(f'Resultado de argumentos por default: {miFuncionLambda()}')

#usar *args y **kwargs (argumentos variables)


miFuncionLambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'Resultado de argumentos variables: {miFuncionLambda(1, 2, 3, a=5, b=6)}')

# funciones lambda con argumentos, args variables y variables por default

miFuncionLambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado funcion lambda: {miFuncionLambda(1, 2, 4, 5, 6, 7, d=5, f=6)}')



