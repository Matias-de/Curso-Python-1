#un closure es una funcion que define a otra, y la puede retornar
#la funcion anidada puede acceder a las variables locales definidas
# en la funcion principal o externa

#funcion principal

#def operacion(a,b):
#definir una funcion interna
#   def sumar():
#      return a + b

#retornar la funcion
# return sumar


#funcion principal
def operacion(a, b):
    #definimos una funcion lambda interna
    return lambda: a + b


miFuncionClosure = operacion(5, 2)
print(f'Resultado de la funcion closure: {miFuncionClosure()}')

#llamar la funcion regresada al vuelo

# print(f'Resultado funcion closure al vuelo: {operacion(2, 5)()}')
