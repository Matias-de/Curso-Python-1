#ejemplo de herencia simple

class ListaSimple:

    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregarElemento(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'


class ListaOrdenada(ListaSimple):

    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregarElemento(self, elemento):
        super().agregarElemento(elemento)
        #Ordenamos el nuevo elemento
        self.ordenar()


#solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)

        #una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        #validamos si el elemento es entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    #sobreescribir el metodo agregar
    def agregarElemento(self, elemento):
        self._validar(elemento)
        #una vez validado lo agregamos a la lista
        super().agregarElemento(elemento)


#Lista de enteros Ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass




listaSimple = ListaSimple([5, 3, 6, 8])
print(listaSimple)
listaOrdenada = ListaOrdenada([4, 6, 9, 3, 10, -1])
print(listaOrdenada)
listaOrdenada.agregarElemento(-14)
print(listaOrdenada)
print(len(listaOrdenada))
#lista enteros
listaEnteros = ListaEnteros([3, 1, 2, 4])
print(listaEnteros)
#lista enteros ordenada
listaEnterosOrdenada = ListaEnterosOrdenada([4, 5, -1, 10, 14])
print(listaEnterosOrdenada)
listaEnterosOrdenada.agregarElemento(-20)
print(listaEnterosOrdenada)
#saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
#MRO (Method Resolution Order)
print(ListaEnterosOrdenada.mro())
#isinstance
print(f'Es entero?: {isinstance(10, int)}')
print(f'Es cadena?: {isinstance('str', str)}')
print('Es lista ent ord?', isinstance(listaEnterosOrdenada, ListaEnterosOrdenada))
print('Es lista ent?', isinstance(listaEnterosOrdenada, ListaEnteros))
print('Es lista ord?', isinstance(listaEnterosOrdenada, ListaOrdenada))
print('Es lista simple?', listaEnterosOrdenada, ListaSimple)
print('Es object?', isinstance(listaEnterosOrdenada, object))
print('Es de varios tipos?', isinstance(listaEnterosOrdenada, (ListaEnteros, ListaSimple, ListaOrdenada)))
