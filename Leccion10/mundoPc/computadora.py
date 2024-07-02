from mundoPc.monitor import Monitor
from mundoPc.raton import Raton
from mundoPc.teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, mouse):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = mouse

    @property
    def idComputadora(self):
        return self._idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f''' 
        {self._nombre} : {self._idComputadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    monitor1 = Monitor('Samsung', 29)
    teclado1 = Teclado('Acer', 'USB')
    raton = Raton('USB', 'HP')
    computadora = Computadora('HP', monitor1, teclado1, raton)
    raton2 = Raton('Bluethoot', 'Acer')
    teclado2 = Teclado('HP', 'Inalambrico')
    monitor2 = Monitor('LG', 32)
    computadora2 = Computadora('Asus', monitor2, teclado2, raton2)
    print(computadora)
    print(computadora2)
