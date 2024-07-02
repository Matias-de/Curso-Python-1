#context manager
class ManejoArchivos: # se pueden usar para mas recursos como base de datos etc
    def __init__(self, nombreArchi):
        self._nombre = nombreArchi

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self._nombre = open(self._nombre, 'r', encoding='utf8')
        return self._nombre

    def __exit__(self, tipoExcepcion, valorExcepcion, textoError):
        print('Cerramos el recurso'.center(50,'-'))
        if self._nombre:
            self._nombre.close()

