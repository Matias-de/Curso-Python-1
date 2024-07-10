#scope

variableGlobal = 'Variable Global'


def imprimir():
    #acceder a una variable global
    global variableGlobal
    print(f'Variable global desde funcion: {variableGlobal}')
    # definicion de variable local
    variableLocal = 'Variable local'
    print(f'Variable local desde funcion: {variableLocal}')

    def funcionAnidada():
        print(f'Variable local dentro de la funcion anidada: {variableLocal}')

    variableGlobal = 'Nuevo Valor de la variable Global'

    funcionAnidada()


imprimir()
print(f'Variable global fuera de la funcion: {variableGlobal}')
