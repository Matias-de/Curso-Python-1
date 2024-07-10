class Persona:
    contadorPersonas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


#mostrar los atributos de un objeto

persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__ )

#crear un atributo en el momento
print(persona1.contadorPersonas) #accediendo al atributo de clase
persona1.contadorPersonas = 10
#no es posible modificarlo con el objeto, sino con la clase
print(persona1.__dict__ )
#el atributo anterior oculta el atributo de clase
print(Persona.contadorPersonas) #atributo de clase
print(persona1.contadorPersonas) #atributo de persona1
persona2 = Persona('Carla', 'Gomez')
print(persona2.__dict__ )
#asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(persona2.contador2)























