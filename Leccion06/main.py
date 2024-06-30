def listarNombres(*args): #argumentos variables
    for arg in args:
        print(arg)


listarNombres('Carlos', 'Juan', 'Karla', "Maria")
listarNombres(2, 4, 5)

def listarTerminos(**keywargs): #recibir diccionario variable
    for clave, valor in keywargs.items():
        print(f'Clave: {clave}; Valor: {valor}')


listarTerminos(IDE = "Integrated development Enviroment", PK = "Primary Key", añosLuto = 34)

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres= ["juan", 'Carla', "Guillermo"]
desplegarNombres((9876, 97986)) #al ponerle parentesis lo toma como tupla y lo acepta sin tirar error
desplegarNombres([234234.23, 453453.3]) #se crea lista al ponerlo entre corchetes


print("-----------------------RECURSIVIDAD---------------------")
def factorial(numero):
    if numero==1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 3
resultado = factorial(numero)
print(f'El factorial de {numero} es: {resultado}')


