from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._idOrden = Orden.contador_ordenes
        self._productos = list(productos)

    @property
    def idOrden(self):
        return self._idOrden

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productosStr = ''
        for producto in self._productos:
            productosStr += producto.__str__() + ' | '
        return f'ORDEN[Id orden: {self._idOrden}, \nProductos: {productosStr}]'


if __name__ == '__main__':
    producto1 = Producto('Pantalon', 340)
    producto2 = Producto('Remera', 155.4)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)