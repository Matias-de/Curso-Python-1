#manejo valores infinitos
import math
from decimal import Decimal
infinitoPositivo = float('inf')
#print(f'infinito positivo: {infinitoPositivo}')
#print(f'Es infinito?: {math.isinf(infinitoPositivo)}')
infinitoNegativo = float('-inf')
#print(f'infinito negativo: {infinitoNegativo}')
#print(f'Es infinito?: {math.isinf(infinitoNegativo)}')

#usando la lib math

#infinitoPositivo = math.inf
#print(f'infinito positivo: {infinitoPositivo}')
#print(f'Es infinito?: {math.isinf(infinitoPositivo)}')
#infinitoNegativo = -math.inf
#print(f'infinito negativo: {infinitoNegativo}')
#print(f'Es infinito?: {math.isinf(infinitoNegativo)}')


#usando Decimal

infinitoPositivo = Decimal('Infinity')
print(f'infinito positivo: {infinitoPositivo}')
print(f'Es infinito?: {math.isinf(infinitoPositivo)}')
infinitoNegativo = Decimal('-infinity')
print(f'infinito negativo: {infinitoNegativo}')
print(f'Es infinito?: {math.isinf(infinitoNegativo)}')
