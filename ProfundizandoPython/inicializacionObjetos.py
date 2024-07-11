#orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador de la clase Padre')

    def metodo(self):
        print('Metodo clase Padre')


class Hijo(Padre):
    #se manda a llamar el metodo init de la clase padre
    #siempre y cuando la clase hija no defina su propio init
    def __init__(self):
        #podemos llamar al init de la clase padre
        super().__init__()
        print('inicializador clase Hijo')

    def metodo(self):
        print('Metodo sobreescrito en la clase hija')


hijo1 = Hijo()
hijo1.metodo()