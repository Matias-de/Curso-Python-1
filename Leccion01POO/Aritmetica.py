class Aritmetica:
    """
    Clase Aritmetica para realizar operaciones de sumar, restar, etc
    """

    def __init__(self, operandoA, operandoB):
        self._operandoA = operandoA
        self._operandoB = operandoB

    @property
    def operandoA(self):
        return self._operandoA

    @operandoA.setter
    def operandoA(self, operandoA):
        self._operandoA = operandoA

    @property
    def operandoB(self):
        return self._operandoB

    @operandoB.setter
    def operandoB(self, operandoB):
        self._operandoB = operandoB

    def sumar(self):
        return self._operandoA + self._operandoB

    def restar(self):
        return self._operandoA - self._operandoB

    def multiplicar(self):
        return self._operandoA * self._operandoB

    def dividir(self):
        return self._operandoA / self._operandoB


aritmetica1 = Aritmetica(5, 3)

print(f'SUMA: {aritmetica1.sumar()}')
print(f'RESTA: {aritmetica1.restar()}')
print(f'MULTIPLICAR: {aritmetica1.multiplicar()}')
print(f'DIVIDIR: {aritmetica1.dividir(): .2f}') # : .2f cant de puntos flotantes a mostrar
