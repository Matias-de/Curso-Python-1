class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcularVolumen(self):
        return self.ancho * self.profundo * self.alto

    def toString(self):
        print(f'CUBO[Ancho: {ancho}, Alto: {alto}, Profundidad: {profundo}]')


ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundo = int(input('Ingrese la profundidad: '))
cubito1 = Cubo(ancho, alto, profundo)
cubito1.toString()
print(f'Volumen Cubo: {cubito1.calcularVolumen()}')

ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundo = int(input('Ingrese la profundidad: '))
cubito2 = Cubo(ancho, alto, profundo)
cubito2.toString()
print(f'Volumen Cubo: {cubito2.calcularVolumen()}')

