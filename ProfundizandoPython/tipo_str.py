# profundizando tipo string
import math
from mi_clase import MiClase

#concatenacion automatica
#variable = 'Adios'
#mensaje = 'Hola' + ' Mundo' + variable #no se pueden concatenar variables de este modo
#mensaje += 'Universidad' 'Python'
#print(mensaje)

#pedir descripcion de metodos o tipos

#help(math.isnan)
#help(str)

#En help aparece lo que se documento con el docstring en la clase

#help(MiClase)

#print(MiClase.__doc__)  #muestra el docstring de la clase, ni de metodos ni de atributos
#print(MiClase.__init__.__doc__)  # muestra la documentacion del metodo init (gracias al __doc__)
#print(MiClase.miMetodo.__doc__)  #muestra solo la documentacion del metodo 'miMetodo'
# las clases se deben autodocumentar con el codigo, debe ser facil de leer, la documentacion debe ser la minima

#str inmutables en Ph
#mensaje1 = 'hola mundo'
#mensaje2 = mensaje1.capitalize()
#print(f'mensaje 1: {mensaje1}, id: {id(mensaje1)}')
#print(f'mensaje2: {mensaje2}, id: {id(mensaje2)}')
#mensaje1 += 'adios'
#print(f'mensaje 1: {mensaje1}, id: {id(mensaje1)}') #al modificar la variable cambia su direccion de memoria
#y se crea un nuevo objeto, INMUTABLE = no modificable, por cada modificacion se genera un nuevo objeto

#help(str.join)

#metodo join para juntar cadenas

#tuplaStr = ('Hola', 'Mundo', 'Universidad', 'Python')
#mensaje = ' '.join(tuplaStr)
#print(mensaje)
#listaCursos = ['Java', 'Python', 'Angular', 'Spring']
#mensaje = ', '.join(listaCursos)
#print(mensaje)
#cadena = 'HolaMundo'
#mensaje = '. '.join(cadena)
#print(mensaje)
#diccionario = {'nombre': 'Carlos', 'apellido': 'Perez', 'edad': '18'}
#llaves = '-'.join(diccionario.keys())
#valores = '-'.join(diccionario.values())
#print(f'Llaves: {llaves}, {type(llaves)}')
#print(f'valores: {valores}, {type(valores)}')

#help(str.split)

#cursos = 'Java Python JavaScript Angular Spring Excel'
#listaCursos = cursos.split()
#print(listaCursos)

#cursosSeparadosXComa = 'Java, Python, JavaScript, Angular, Spring, Excel'
#listaCursos = cursosSeparadosXComa.split(', ')
#print(listaCursos)

#listaCursos = cursosSeparadosXComa.split(', ',2) # se separan solo las primeras dos palabras
#print(listaCursos)

#dar formato a un str

nombre = 'Juan'
edad = 28
#mensaje = 'Mi nombre es %s y mi edad es %s' % (nombre, edad)
#print(mensaje)

#persona = ('Karla', 'Gomez', 5000.00)
#mensaje = 'Hola %s %s, tu sueldo es: %.2f' % persona
#print(mensaje)
#mensaje = 'Hola %s %s, tu sueldo es: %.2f'
#print(mensaje % persona)

#metodo format
sueldo = 3000
#{} = placeholders
mensaje = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)
#print(mensaje)

mensaje = 'Sueldo: {2:.2f}, Edad: {1}, Nombre: {0}'.format(nombre, edad, sueldo)
#print(mensaje)

mensaje = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, s=sueldo, e=edad)
#print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 5000.50}

mensaje = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}'.format(dic= diccionario)
#print(mensaje)

#f'' string
mensaje = f'Nombre: {nombre}, edad: {edad}, Sueldo: {sueldo}'
#print(mensaje)

#metodo print

print(nombre, edad, sueldo, sep=', ')



