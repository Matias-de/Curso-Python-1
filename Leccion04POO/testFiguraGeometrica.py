from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion Objeto Cuadrado'.center(50, '-'))

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.__str__())
print(f'Calculo Area: {cuadrado1.calcularArea()}')

#MRO - Method Resolution Order
#print(Cuadrado.mro()) #muestra el orden en que se acceden los datos (camino de migas)
#el camino de migas se puede modificar segun como se declaran las clases padre en la declaracion de la clase hija

print('Creacion objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 6, 'Azul')
print(rectangulo1)
print(f'Calculo del Area: {rectangulo1.calcularArea()}')
