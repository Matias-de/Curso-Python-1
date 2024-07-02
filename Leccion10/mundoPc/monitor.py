class Monitor:
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    def __str__(self):
        return f'Monitor: Id: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitor1 = Monitor('Samsung', 29)
    monitor2 = Monitor('LG', 32)
    print(monitor1)
    print(monitor2)
