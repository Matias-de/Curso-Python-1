class Persona:
    contadorPersonas = 0

    @classmethod
    def _generarSiguienteValor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas

    def __init__(self, nombre, edad):
        Persona.contadorPersonas = Persona._generarSiguienteValor()
        self._idPersona = Persona.contadorPersonas
        self._nombre = nombre
        self._edad = edad

    @property
    def idPersona(self):
        return self._idPersona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'Persona[ID: {self._idPersona}, Nombre: {self._nombre}, Edad: {self._edad}]'


persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Carla', 30)
print(persona2)
