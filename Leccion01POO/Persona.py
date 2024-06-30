class Persona:
    def __init__(self, nombre, apellido, edad):  # __ = duder
        self._nombre = nombre  #poner un _ al principio significa que es privado
        self._apellido = apellido
        self._edad = edad

    # self.args = args #robustecer la creacion de clases con tuplas y mapas
    #  self.kwargs = kwargs

    @property  # decorador, como un override, pero permite bloquear el acceso a un metodo, solo haciendolo pasar por este get
    def nombre(self):  #esto es un get
        return self._nombre

    @nombre.setter  #esto es un setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):  #self = this
        print(f'''Persona[Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}]''')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} fue eliminado/a')


if __name__ == '__main__':
    persona1 = Persona('Carlos', 'Vega', 54)
    persona1.mostrarDetalle()
    #aunque pongas el _ o doble _ es solo una sugerencia, se puede igualmente modificar
    print(persona1.nombre)
    persona1.nombre = 'Roberto'
    persona1.apellido = 'Mouras'
    persona1.edad = 75
    persona1.mostrarDetalle()

#si un atributo tiene un _ adelante y solo el get (y no el set) se denomina variable de solo lectura, o "Read Only"
