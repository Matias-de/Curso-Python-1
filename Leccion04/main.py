

for letra in "Holanda":
    if letra == "a":
        print(f'Letra encontrada: {letra}')
        break
    else:
        print("FIN CICLO FOR") #opcional (es terrible)


#for i in range(6):
#   if i % 2 == 0:
#      print(f'Valor: {i}')


for i in range(6):
    if i % 2 !=0:
        continue
    else:
        print(f'Valor: {i}')