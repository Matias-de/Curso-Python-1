class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrdenes = Orden.contadorOrdenes
        self._computadoras = computadoras

    @property
    def idOrdenes(self):
        return self._idOrdenes

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregarComputadoras(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoraStr = ''
        for computadora in self._computadoras:
            computadoraStr += computadora.__str__()
        return f'''
            Orden: {self._idOrdenes}
            Computadoras: {computadoraStr}
            '''



