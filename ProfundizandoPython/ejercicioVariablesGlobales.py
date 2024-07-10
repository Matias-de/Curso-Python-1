#definir variable global

contador = 0


def mostrarContador():
    print(contador)


def modificarContador(c):
    global contador
    contador = c


modificarContador(5)
mostrarContador()
