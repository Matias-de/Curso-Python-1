#leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
palabras = []
with urlopen(peticion) as mensaje:
# contenido = mensaje.read()
    #contenido = mensaje.read().decode('utf-8')
    #print(contenido)
    #for linea in mensaje:
     #   palabrasPorlinea = linea.decode('utf-8').split()
        #print(palabrasPorlinea)
      #  for palabra in palabrasPorlinea:
       #     palabras.append(palabra)
    contenido = mensaje.read().decode('utf-8')

#contar ocurrencias de una cadena
#print(contenido.count('Universidad'))
#convertir a mayusculas una cadena
#print(contenido.upper())
#convertir a minusculas una cadena
#print(contenido.lower())

#python existe en la cadena 'contenido'?

#print('python'.lower() in contenido.lower())

#startswith-inicio con
#print(contenido.startswith('En GlobalMentoring.com.mx'))

#endswith -termina con
#print('Termina con: ', contenido.endswith('GlobalMentoring.com.mx'))

mensaje = 'Hola mundo'
#print(mensaje.lower().islower())
#print(mensaje.isupper())

#print(palabras)
#with open('nuevo archivo.txt', 'w', encoding='utf-8') as archivo:
 #   archivo.write(contenido)


 #alinear cadenas


 #centrar un string -center

titulo = 'Sitio web de GlobalMentoring.com.mx'
#print(len(titulo))
#print(titulo.center(50, '-'))
#print(titulo.center(len(titulo)+10, '-'))
#print(titulo.ljust(len(titulo)+10,'-'))
#print(titulo.rjust(len(titulo)+10,'-'))

#reemplazar contenido en un str

#print(contenido.replace(' ', '-'))

#eliminar caracteres al inicio y final de un str -strip

titulo = ' *** GlobalMentoring.com.mx *** '
print('Titulo original: ', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada: ', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada: ', titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada: ', titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada: ', titulo)
titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada: ', titulo)


