class Rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la Altura: '))
rectangulo1 = Rectangulo(base, altura)
print(f'Area rectangulo: {rectangulo1.calcularArea()}')
base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la Altura: '))
rectangulo2 = Rectangulo(base, altura)
print(f'Area rectangulo: {rectangulo2.calcularArea()}')