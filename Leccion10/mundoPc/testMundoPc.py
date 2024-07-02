from mundoPc.computadora import Computadora
from mundoPc.monitor import Monitor
from mundoPc.orden import Orden
from mundoPc.raton import Raton
from mundoPc.teclado import Teclado

monitor1 = Monitor('Samsung', 29)
teclado1 = Teclado('Acer', 'USB')
raton = Raton('USB', 'HP')
computadora = Computadora('HP', monitor1, teclado1, raton)
raton2 = Raton('Bluethoot', 'Acer')
teclado2 = Teclado('HP', 'Inalambrico')
monitor2 = Monitor('LG', 32)
computadora2 = Computadora('Asus', monitor2, teclado2, raton2)
computadoras1 = [computadora, computadora2]
orden1 = Orden(computadoras1)
teclado3 = Teclado('Gamer', 'Inalambrico')
raton3 = Raton('USB', 'Logitech')
monitor3 = Monitor('Asus', 28)
computadora3 = Computadora('Shenglong', monitor3, teclado3, raton3)
#print(orden1)
orden1.agregarComputadoras(computadora3)
print(orden1)
computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)