#print(dir(__builtins__))
#help(zip)

numeros1 = [1, 2, 3]
letras1 = ['a', 'b', 'c', 'd']
identificadores = 321, 322, 323, 324, 325
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezcla = zip(numeros1, letras1, identificadores, conjunto)
print(list(mezcla))
#print(tuple(zip(numeros1, letras1)))

#iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros1, letras1, identificadores, conjunto):
    print(f'Numero: {numero}, Letra: {letra}, id: {id}, AleatorioSet: {aleatorio}')

nuevaLista = []
for numero, letra, id, aleatorio in zip(numeros1, letras1, identificadores, conjunto):
    nuevaLista.append(f'{id}-{numero}-{letra}-{aleatorio}')

print(nuevaLista)

#unzip

mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros1, letras1 = zip(*mezcla)
print(numeros1)
print(letras1)

#ordenamiento usando zip

letras = ['c', 'd', 'a', 'e', 'b']
numeros1 = [3, 2, 4, 1, 0]

mezcla = zip(letras, numeros1)
#sin ordenar
print(tuple(mezcla))
#ordenando
print(sorted(zip(letras, numeros1))) #se ordena segun el primer atributo que se le pase, en este caso, se ordena por letras

#crear un diccionario con zip

llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# actualizar elemento de un diccionario
llave = ['Edad']
valor = [20]
diccionario.update(zip(llave, valor))
print(diccionario)
































































