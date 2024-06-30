from Persona import Persona
print('Creacion objetos'.center(50, '-'))
if __name__ == '__main__':
    persona1 = Persona('Karla', 'Gomez', 30)
    persona1.mostrarDetalle()

print('Eliminacion objetos'.center(50, '-'))
print(persona1.__del__())
