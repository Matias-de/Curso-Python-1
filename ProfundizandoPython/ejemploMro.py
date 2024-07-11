class Clase1:
    def __init__(self):
        print('Inicializador Clase1')

    def metodo(self):
        print('Metodo Clase1')


class Clase2(Clase1):
    def __init__(self):
        print('Inicializador Clase2')
        super().__init__()

    def metodo(self):
        print('Metodo Clase2')
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print('Inicializador Clase3')
        super().__init__()



    def metodo(self):
        print('Metodo Clase3')
        super().metodo()


class Clase4(Clase2, Clase3):  #se llama el init de la Clase2 (La primera que se pone), la cual sera la mas importante
    def metodo(self):
        print('Metodo Clase4')
        super().metodo()

#crear objeto Clase4

clase4 = Clase4()
#__bases__
print(Clase4.__bases__)

#mro
print(Clase4.mro())
#cual metodo se ejecuta

clase4.metodo()
