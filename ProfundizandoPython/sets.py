# sets

#los elementos de un set deben ser inmutables, no puede guardar listas por ejemplo
conjunto = {'Juan', True, 18}
print(conjunto)

#set vacio
conjunto = set() # si se pone conjunto = {} genera un mapa no un set

conjunto.add('Juan')
print(conjunto)
#contiene valores unicos
conjunto.add('Juan')
print(conjunto)

#crear un set a partir de un iterable

conjunto = set([4, 5, 7, 8, 4])

print(conjunto)

#agregar mas elementos con otro set

conjunto2 = {100, 200, 300, 100}
conjunto.update(conjunto2)
print(conjunto)

conjunto.update([20, 30, 40, 40])
print(conjunto)

#copiar un set (solo de referencias

copiaConjunto = conjunto.copy()
print(copiaConjunto)

#verificar igualdad

print(f'Es igual en contenido? {conjunto == copiaConjunto}')
print(f'Es la misma referencia?: {conjunto is copiaConjunto}')

peloNegro = {'Juan', 'Carla', 'Pedro', 'Maria'}
peloRubio = {'Lorenzo', 'Laura', 'Marco'}
ojoscafe = {'Carla', 'Laura'}
menores30 = {'Juan', 'Carla', 'Maria'}
#todos con ojos cafe y pelo rubio (union)
print(ojoscafe.union(peloRubio))
# invertir el orden con el mismo resultado (conmutativo)
print(peloRubio.union(ojoscafe))

# interseccion

#recuperar solo las personas con ojos cafe y pelo rubio

print(ojoscafe.intersection(peloRubio))

#difference | pelo negro sin ojos cafe (no es conmutativa)

print(peloNegro.difference(ojoscafe)) #solo las que se encuentran en el primer set y no esten en el segundo

#diferencia simetrica | pelo negro u ojos cafe, pero no ambos

print(peloNegro.symmetric_difference(ojoscafe)) # conmutativa


#preguntar si un set esta contenido en otro

#revisamos si los elementos del primer conjunto estan contenidos en el segundo

print(menores30.issubset(peloNegro))

#preguntar si un set contiene a otro set (superset)
#revisar si los elementos del primer set estan contenidos en el segundo set

print(menores30.issuperset(peloNegro))

#preguntar si los de pelo negro no tienen pelo rubio (distjoint)

print(peloNegro.isdisjoint(peloRubio))

















