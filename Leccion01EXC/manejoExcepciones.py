from NumerosIdenticosException import NumerosIdenticosException

resultado = None  #si las variables se usan fuera del try catch se declaran arriba

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros identicos')  #throws
    resultado = a / b
except ZeroDivisionError as e:  #catch
    print(f'ZeroDivisionError; Ocurrió un error: {e}, {type(e)}')
except ValueError as e2:
    print(f'ValueError; Ocurrió un error: {e2}, {type(e2)}')
except Exception as e3:  #primero las excepciones hijas, después el padre
    print(f'Exception; Ocurrió un error: {e3}, {type(e3)}')
else:
    print('no se arrojo ninguna excepción')
finally:
    print('Ejecución desde Finally')
print(resultado)
print('Continuamos...')
