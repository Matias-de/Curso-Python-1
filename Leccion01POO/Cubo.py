class Cubo:
    def __init__(self, ancho, alto, profundo):
        self._ancho = ancho
        self._alto = alto
        self._profundo = profundo

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho2):
        self._ancho = ancho2

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto2):
        self._alto = alto2

    @property
    def profundo(self):
        return self._profundo

    @profundo.setter
    def profundo(self, profundo2):
        self._profundo = profundo2

    def calcularVolumen(self):
        return self._ancho * self._profundo * self._alto

    def toString(self):
        print(f'CUBO[Ancho: {self._ancho}, Alto: {self._alto}, Profundidad: {self._profundo}]')


ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundo = int(input('Ingrese la profundidad: '))
cubito1 = Cubo(ancho, alto, profundo)
cubito1.toString()
print(f'Volumen Cubo: {cubito1.calcularVolumen()}')

ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundo = int(input('Ingrese la profundidad: '))
cubito2 = Cubo(ancho, alto, profundo)
cubito2.toString()
print(f'Volumen Cubo: {cubito2.calcularVolumen()}')

