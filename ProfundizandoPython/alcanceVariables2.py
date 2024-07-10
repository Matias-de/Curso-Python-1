def funcionExterna():
    variableLocalExterna = 'Variable local externa'

    def funcionAnidada():
        variableLocalAnidada = 'Variable local anidada'

        nonlocal variableLocalExterna
        variableLocalExterna = 'Nuevo valor variable externa'

    funcionAnidada()

    print(f'Valor variable local externa: {variableLocalExterna}')

funcionExterna()