from cursor_del_pool import CursorDelPool
from persona import Persona
from logger_base import log
from usuario import Usuario


class UsuarioDAO:
    """
    DAO= Data Access Object para la tabla usuario
    CRUD = Create-Read-Update-Delete para la tabla usuario
    """

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug(f'Seleccionando usuarios..')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
        return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Se insertara el usuario: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Se actualizara el usuario: {usuario}')
            valores = (usuario.username, usuario.password, usuario.idUsuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Se eliminara al usuario: {usuario}')
            valores = (usuario.idUsuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


if __name__ == '__main__':
    #insertar un registro
    #usuario = Usuario(username='pnajera', password='654')
    #usuariosInsertadas = UsuarioDAO.insertar(usuario)
    #log.debug(f'Usuarios Insertadas: {usuariosInsertadas}')

    #actualizar un registro
    #usuario = Usuario(1, 'jchola', '345')
    #usuariosActualizadas = UsuarioDAO.actualizar(usuario)
    #log.debug(f'usuarios Actualizadas = {usuariosActualizadas}')

    #Eliminar un registro
    usuario = Usuario(idUsuario=3)
    usuariosActualizadas = UsuarioDAO.eliminar(usuario)
    log.debug(f'usuarios Actualizadas = {usuariosActualizadas}')


    #seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
