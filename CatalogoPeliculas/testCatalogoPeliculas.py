from Dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPeliculas as catalogoPelicula

eleccion = 0

while eleccion != 4:
    try:
        print(f'''Opciones:
        1. Agregar Película
        2. Listar Películas
        3. Eliminar Catálogo de Películas
        4. Salir''')
        eleccion = int(input('Escribe tu opción: (1-4): '))
        if eleccion == 1:
            peliAux = Pelicula(str(input('Proporciona la película: ')))
            catalogoPelicula.agregarPelicula(peliAux)
        elif eleccion == 2:
            print(catalogoPelicula.listarPeliculas())
        elif eleccion == 3:
            print(catalogoPelicula.eliminar())
        elif eleccion != 4:
            print('ERROR, OPCION INVALIDA; REINTENTE...')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = 0
else:
    print('Fin del Programa..')
