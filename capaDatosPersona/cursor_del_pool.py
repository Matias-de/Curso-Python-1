from conexion import Conexion
from logger_base import log


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExepcion, valorExepcion, detalle):
        log.debug('Se ejecuta metodo __exit__')
        if valorExepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una exepcion, se hace rollback: {valorExepcion} {tipoExepcion} {detalle}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('En with')
        cursor.execute('SELECT * FROM persona ORDER BY id_persona')
        log.debug(cursor.fetchall())