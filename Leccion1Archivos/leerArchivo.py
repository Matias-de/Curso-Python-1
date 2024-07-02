#tendria que haber un try-catch
archivo = open('prueba.txt', 'r', encoding='utf8')
#r para leer
# a anexar informacion (agregar al final) -append, crea si no existe
# w escribe informacion, crea si no existe
# x crea el archivo especificado, pero manda una excepcion si no existe
# + t para archivo de texto
# + binario (fotos, pdf, etc)
# w+ escribir y leer
# r+ abrir (leer) y escribir
#print(archivo.read()) si se pone esto despues no se pueden consumir mas caracteres
    #leer algunos caracteres
#print(archivo.read(10))
#print(archivo.read(10))
    #leer lineas completas
#print(archivo.readline())
#print(archivo.readline())
    #iterar archivo
#for linea in archivo:
   # print(linea)

    #leer lineas
#print(archivo.readlines())
    #acceder a una linea de la lista
#print(archivo.readlines()[2])
    #abrir un nuevo archivo
#a - agregar al final

archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()
print('se ha terminado el proceso de leer y copiar archivos')