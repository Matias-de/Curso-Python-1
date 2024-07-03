import os


class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.rutaArchivo, 'a', encoding='utf8') as archivo:
            archivo.write(pelicula.nombre + '\n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.rutaArchivo, 'r', encoding='utf8') as archivo:
            return f'''Catalogo peliculas: 
            {archivo.read()}
            '''

    @classmethod
    def eliminar(cls):
        os.remove(cls.rutaArchivo)
        return f'Archivo eliminado: {cls.rutaArchivo}'