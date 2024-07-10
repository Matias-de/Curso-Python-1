# funciones = first class citizens

#definir funcion


def sumar(a, b):
    return a + b


#asignar una funcion a una variable (sin parentesis)

miFuncion = sumar

#verificar el tipo de la variable

#print(type(miFuncion))

#llamar la funcion a traves de la variable

resultado = miFuncion(10,4)
print(resultado)


#funcion como argumento

def operacion(a, b, sumarArg):
    print(f'Resultado sumar: {sumarArg(a, b)}')

operacion(10,5, sumar)

#retornar una funcion desde otras funciones

def retornarFuncion():
    #retorno una funcion
    return sumar

miFuncion = retornarFuncion()
print(f'Resuntado funcion retornada: {miFuncion(5,7)}')







