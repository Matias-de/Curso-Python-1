#ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor invalido de ancho: {ancho}')
        if self._validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor invalido de alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor invalido de ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor invalido de alto: {alto}')

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica[Alto: {self._alto}, Ancho: {self._ancho}]'

    def _validarValor(self, valor):
        return True if 0 < valor <= 10 else False
