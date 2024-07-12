#transformar de manera programatica la clase
#similar a los decoradores de funciones (es metaprogramacion)
import inspect


def decoradorRepr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    #revisamos los atributos de la clase con el metodo vars
    atributos = vars(cls)
    #itrerar cada atributo
    #for nombre, atributo in atributos.items():
    #   print(nombre, atributo)

    #revisar si se ha sobreescrito el metodo init
    if '__init__' not in atributos:
        raise TypeError(f'La clase {cls.__name__} no ha sobreescrito el init')

    firmaInit = inspect.signature(cls.__init__)
    print(f'Firma metodo init: {firmaInit}')
    #recuperamos los parametros menos el self
    parametrosInit = list(firmaInit.parameters)[1:]
    print(f'Parametros init: {parametrosInit}')
    #revisamos si cada parametro tiene un property
    for parametro in parametrosInit:
        #property es un valor de tipo buildt-in para preguntar si se esta utilizando el decorador
        esMetodoProperty = isinstance(atributos.get(parametro), property)
        if not esMetodoProperty:
            raise TypeError(f'No existe un metodo property para el parametro: {parametro}')

    #crear el metodo repr dinamicamente
    def metodoRepr(self):
        #obtenemos el nombre de la clase dinamicamente
        nombreClase = self.__class__.__name__

        #obtenemos los nombres de las propiedades y sus valores dinamicamente
        #Expresion generadora, crear nombre_atributo=valor_atributo
        generadorArg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametrosInit)
        #lista del generador
        listaArg = list(generadorArg)
        print(f'Lista del generador: {listaArg}')
        #Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(listaArg)
        print(f'Argumentos del metodo repr: {argumentos}')
        #creamos la forma del metodo __repr__ sin el nombre
        resultadoMetodoRepr = f'{nombreClase}({argumentos})'
        return resultadoMetodoRepr
    #agregar dinamicamente el metodo repr a la clase
    setattr(cls, '__repr__', metodoRepr)

    return cls


@decoradorRepr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    def __repr__(self):
        return f'{self.__class__.__name__}()'


persona1 = Persona('Juan', 'Perez', 28)
print(persona1)
persona2 = Persona('Carla', 'Gomez', 30)
print(persona2)
#tiene los metodos de propiedad nombre, apellido, repr
print(dir(Persona))
#tiene el metodo repr sobreescrito
codigoRepr = inspect.getsource(persona1.__repr__)
print(codigoRepr)