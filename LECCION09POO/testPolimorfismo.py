from Empleado import Empleado
from Gerente import Gerente


def imprimirDetalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrarDetalles())
    print(objeto.departamento) if isinstance(objeto, Gerente) else print('No es un Gerente')


empleado = Empleado('Carlos', 5500.5)
imprimirDetalles(empleado)
gerente = Gerente('Karla', 6000, 'Sistemas')
imprimirDetalles(gerente)
