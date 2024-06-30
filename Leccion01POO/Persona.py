class Persona:
    def __init__(self, nombre, apellido, edad):  # __ = duder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):  #self = this
        print(f'''Persona[Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}]''')


persona1 = Persona('Carlos', 'Vega', 54)
persona1.mostrarDetalle()
