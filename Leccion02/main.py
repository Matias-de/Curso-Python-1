print('Proporcione los siguientes datos del libro: ')
nombreLibro = input("Proporciona el nombre: ")
idLibro = int(input("Proporcione el ID: "))
precio = float(input("Proporcione el Precio: "))
envioGratis = input("Proporcione si el envio es gratuito (True/False): ")

if envioGratis == "True" or envioGratis == "true":
    envioGratis = True
elif envioGratis == "False" or envioGratis == "false":
    envioGratis = False
else:
    print("error")

print(f'''
        Nombre: {nombreLibro}
        ID: {idLibro}
        Precio: {precio}
        Envio Gratuito: {envioGratis}
''')
