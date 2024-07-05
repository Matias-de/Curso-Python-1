#bool = True/False
#tipos numericos, False para 0, True para todos los demas
#valor = 0
#resultado = bool(valor)
#print(resultado)
#valor = 15
#resultado = bool(valor)
#print(resultado)

#tipo str, False si la cadena esta vacia (''), otro valor True
#valor = ''
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')
#valor = 'holaaa'
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')

#Tipo colecciones, false para colecciones vacias, el resto true

#valor = []
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')
#valor = ['holaaa', 'chauu']
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')

#tupla

#valor = ()
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')
#valor = ('holaaa',)
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')

#diccionario

#valor = {}
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')
#valor = {'nombre':'juan', 'apellido':'perez'}
#resultado = bool(valor)
#print(f'valor: {valor}, Resultado: {resultado}')

variable = 'sdf'
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso verdadero')
else:
    print('Regreso falso')

while variable:
    print('Ejecucion while')
    break #como para que no se rompa nada

else:
    print('fin while')





