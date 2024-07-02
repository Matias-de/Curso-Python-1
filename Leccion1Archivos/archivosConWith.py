from manejoArchivos import ManejoArchivos
#el with permite abrir y cerrar el archivo sin tener un try finally
#with open('prueba.txt', 'r', encoding='utf8') as archivo:

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

