class Rectangulo:
    def __init__(self, base, altura):
        self._altura = altura
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura2):
        self._altura = altura2

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base2):
        self._base = base2

    def calcularArea(self):
        return self._base * self._altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la Altura: '))
rectangulo1 = Rectangulo(base, altura)
print(f'Area rectangulo: {rectangulo1.calcularArea()}')
base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la Altura: '))
rectangulo2 = Rectangulo(base, altura)
print(f'Area rectangulo: {rectangulo2.calcularArea()}')
