from mundoPc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        super().__init__(tipoEntrada, marca)
        self._idRaton = Raton.contadorRatones

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self._idRaton = idRaton

    def __str__(self):
        return f'Raton: Id: {self._idRaton}, Marca: {self._marca}, tipo De Entrada: {self._tipoEntrada}'


if __name__ == '__main__':
    raton = Raton('USB', 'HP')
    print(raton)
    raton2 = Raton('Bluethoot', 'Acer')
    print(raton2)
