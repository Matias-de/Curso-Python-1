class Producto:
    contador_Productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_Productos += 1
        self._idProducto = Producto.contador_Productos
        self._nombre = nombre
        self._precio = precio

    @property
    def idProducto(self):
        return self._idProducto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'PRODUCTO[Id producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio}]'


if __name__ == '__main__':
    producto1 = Producto('Pantalon', 340)
    producto2 = Producto('Remera', 155.4)
    print(producto1)
    print(producto2)
