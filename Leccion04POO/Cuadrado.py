from FiguraGeometrica import *
from Color import *


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)  #especificar el self
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
