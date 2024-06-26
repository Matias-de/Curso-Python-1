class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombreAux):
        self._nombre = nombreAux

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edadAux):
        self._edad = edadAux

    def __str__(self):
        return f'Persona: Nombre: {self._nombre}, Edad: {self._edad}'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, Empleado [Sueldo: {self._sueldo}]'
