#Representacion de objetos(str, repr, format)

#print(dir(object))
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #repr, mas enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre}, apellido={self.apellido})'

    #str es mas para el usuario final u otro sistema
    #la implementacion por default llama al metodo repr
    def __str__(self):
        return f'{self.__class__.__name__}: Nombre: {self.nombre}, Apellido: {self.apellido}'

    #format su implementacion por default es str
    #se manda de forma automatica al usar f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(f'Mi objeto persona1: {persona1!r}')
# str (de manera automatica el print llama al str, si no esta definido llama al repr
print(persona1)
#format
print(f'{persona1}')