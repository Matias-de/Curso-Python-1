#simulacion de sobrecarga de constructores en Python
#otras formas de crear objetos

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crearPersonaVacia(cls):
        return cls(None, None)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

    @classmethod
    def crearPersonaConValores(cls, nombre, apellido):
        return cls(nombre, apellido)

persona1 = Persona('Juan', 'Perez')
personaVacia = Persona.crearPersonaVacia()
personaConValores = Persona.crearPersonaConValores('Carla', 'Gomez')
print(personaVacia)
print(persona1)
print(personaConValores)