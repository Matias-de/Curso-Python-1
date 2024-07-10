#decoradores

#un decorador es una funcion que recibe una funcion y regresa otra

#se utilizan para extender funcionalidad

#1.funcion decorador(a)
#2. funcion a decorar(b)
#3. funcion decorada(c)


def funcionDecoradorA(funcionADecorarB):
    def funcionDecoradaC(*args, **kwargs):
        print('Antes de ejecutar la funcion')
        resultado = funcionADecorarB(*args, **kwargs)
        print('Despues de ejecutar la funcion')
        return resultado
    return funcionDecoradaC


@funcionDecoradorA
def mostrarMensaje():
    print('Hola desde funcion MostrarMensaje')


#mostrarMensaje()


@funcionDecoradorA
def imprimir():
    print('Hola desde imprimir')


#print()
#imprimir()

@funcionDecoradorA
def sumar(a, b):
    return a + b


resultado = sumar(5, 6)

print(f'Resultado de la suma: {resultado}')
