#funciones anidadas


def calculadora(a, b, operacion='sumar'):
    #definir funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    if operacion == 'sumar':
        print(f'Resultado de sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado Restar: {restar(a, b)}')


calculadora(10, 6)
calculadora(10, 2, 'restar')
