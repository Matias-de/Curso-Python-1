class MiClase:
    variableClase = 'Valor variable clase'

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    @staticmethod
    def metodoEstatico():
        print(MiClase.variableClase)

    @classmethod
    def metodoClase(cls):
        print(cls.variableClase)

    def metodoInstancia(self):
        self.metodoClase()
        self.metodoEstatico()


miObjeto1 = MiClase('Variable de Instancia')
miObjeto1.metodoClase()  #contexto dinamico si puede acceder a contexto estatico, no al revez
miObjeto1.metodoInstancia()
