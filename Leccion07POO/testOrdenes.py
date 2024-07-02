from Orden import Orden
from Producto import Producto

producto1 = Producto('Pantalon', 340)
producto2 = Producto('Remera', 155.4)
producto3 = Producto('Medias', 50.00)
producto4 = Producto('Camisa', 200)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto4)
orden2 = Orden(productos2)
print(orden1)
print(orden2)
print(f'Total de la orden1: {orden1.calcularTotal()}')
print(f'Total de la orden2: {orden2.calcularTotal()}')