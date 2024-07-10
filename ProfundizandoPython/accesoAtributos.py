#Ejemplo atributos publicos, protegidos, privados
class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
print(objeto.publico)
#modificar el valor publico
objeto.publico = 'Nuevo valor publico'
print(objeto.publico)
#acceso al valor protegido
#solo dentro de la misma clase o clases hijas
print(objeto._protegido)
#modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)
#acceder al valor privado
#solo se debe acceder desde la clase unicamente
#print(objeto.__privado)
#pero, convierte: objeto._clase__atributoPrivado
print(objeto._MiClase__privado)
#modificar valor privado (no recomendable)
objeto._MiClase__privado = 'nuevo valor privado'
print(objeto._MiClase__privado)



















