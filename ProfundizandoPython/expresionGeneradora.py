#expresion generadora (generador anonimo)
import math


multiplicacion = (valor*valor for valor in range(4))

print(type(multiplicacion))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))


#también se puede pasar un generador a una funcion (sin parentesis)

suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')








