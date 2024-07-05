import math
from decimal import Decimal
#NaN - Not a number
#NaN no es sensible a mayusculas/minusculas
#NaN es un tipo de dato numerico indefinido
a = float('NaN')
#print(f'a: {a}')
#print(f'Es NaN?: {math.isnan(a)}')
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN?: {math.isnan(a)}')