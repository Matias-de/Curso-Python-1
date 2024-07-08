#mapas
#tienen un orden
from pprint import pprint as pp

diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)

#son mutables, pero las llaves son inmutables

#una tupla si se puede usar de llave porque es inmutable

#diccionario = {(1, 2):'valor'}
#print(diccionario)

#se agrega una llave si no se encuentra

diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# no acepta duplicados

diccionario['Nombre'] = 'Carlos'
print(diccionario)

#recuperar elementos indicando la llave

print(diccionario['Nombre'])

#el get recupera una llave, si no existe NO larga excepcion, se puede devolver un valor en caso de que no exista

print(diccionario.get('Estadisticas', 'No se encontro la llave'))

#setdefault si modifica el diccionario, ademas regresa un valor por default(opcional)

nombre = diccionario.setdefault('Nombres', 'Valor por default')
print(diccionario)

#impirimir con pprint

#help(pp)
pp(diccionario, sort_dicts=False)






































