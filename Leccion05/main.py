#definir lista de tipo string
nombres = ["Juan", 'Carla', 'Ricardo', "Maria"]
#imprimir la lista nombres
print(nombres)
#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
#acceder de manera inversa
print(nombres[-1])
print(nombres[-2])
#imprimir rango
print(nombres[0:2]) # no incluye al indice 2, solo el 0 y 1
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) #incluye el 0, 1 y 2
#recorrer desde el indice adecuado hasta el final
print(nombres[0:])
#cambiar un valor
nombres[3] = "Martina"
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("Fin de lista")

#Preguntar cant elementos

print(len(nombres))

#agregar elemento

nombres.append("Lorenzo")
print(nombres)
#insertar elemento en indice especifico
nombres.insert(1, "Octavio") #todos los demas elementos se mueven a la derecha
print(nombres)
nombres.remove("Octavio")
print(nombres)
#remover el ultimo
nombres.pop()
print(nombres)
#eliminar un indice
del nombres[0]
print(nombres)
#limpiar elementos de toda la lista
nombres.clear()
print(nombres)
#borrar lista por completo
del nombres
#print(nombres) tira excepcion, ya no existe.

print("---------------------------------TUPLAS----------------------------")
#son inmutables, no se pueden modificar una vez cargadas, aunque respete el orden

#definir una tupla

frutas = ("Naranja", "Banana", "Pera") #si se agrega un solo elemento, hay que agregar una coma, sino se consideraria solo una string
print(frutas)
#conocer cant elementos
print(len(frutas))
#acceder a un elemento en particular
print(frutas[0])
#navegacion inversa
print(frutas[-1]) #ultimo valor de la tupla

#acceder a un rango
print(frutas[0:2]) #sin incluir ultimo indice

#recorrer elementos

for fruta in frutas:
    print(fruta, end=" ") # el end para cualquier print
else:
    print("\nFin de tupla")

#cambiar valor tupla

#pasar a lista, modificarla y volver a pasarla a una tupla
#PARA QUE USABA TUPLAS SI LAS PASAS A UNA LISTA KAJSDMHASKHJB

frutaLista = list(frutas)
frutaLista[0] = "Manzana"
frutas = tuple(frutaLista)
print("\n", frutas)

print("-----------------------------SET----------------------")
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
#largo
print(len(planetas))
#contiene elemento
print("Marte" in planetas)
#agregar elemento
planetas.add("Tierra")
print(planetas)
planetas.add("Jupiter")
print(planetas)
#eliminar elemento (remove contine excepcion)
planetas.remove("Tierra")
print(planetas)
#eliminar sin que tenga excepcion si no se encuentra en el set
planetas.discard("Jupiter")
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set del programa
del planetas

print("--------------------DICCIONARIOS (mapa)------------------------")

diccionario = {
    'IDE': "Integrated development Environment",
    'OOP': "Object Oriented Programming",
    'DBMS': 'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento
print(diccionario['IDE'])
#otra forma

print(diccionario.get('OOP'))
#modificando elementos
diccionario['IDE'] = "integrated development enviroment"
print(diccionario)
#recorrer elementos
for termino, valor in diccionario.items():
    print(termino,":", valor)
for termino in diccionario.keys():
    print(termino)
for termino in diccionario.values():
    print(termino)

# comprobar elemento existente

print("IDE" in diccionario)
#agregar elemento

diccionario["PK"] = "Primary Key"
print(diccionario)

#remover elemento

diccionario.pop("OOP")
print(diccionario)

#limpiar diccionario

diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario
