from mundoPc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorEntradas = 0

    def __init__(self, marca, tipoEntrada):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorEntradas += 1
        self._idTeclado = Teclado.contadorEntradas

    @property
    def idTeclado(self):
        return self._idTeclado
    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self._idTeclado = idTeclado

    def __str__(self):
        return f'Teclado: Id: {self._idTeclado}, Marca: {self._marca}, tipoEntrada: {self._tipoEntrada}'


if __name__ == '__main__':
    teclado1 = Teclado('Acer', 'USB')
    teclado2 = Teclado('HP', 'Inalambrico')
    print(teclado1)
    print(teclado2)
