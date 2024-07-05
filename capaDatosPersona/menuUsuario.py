import logging
from logger_base import log
from usuario import Usuario
from usuarioDAO import UsuarioDAO

opcion = None

while opcion != 5:
    try:

        print(f'''
    Opciones:
        1. Listar Usuarios
        2. Agregar Usuario
        3. Modificar Usuario
        4. Eliminar Usuario
        5. Salir
        ''')
        opcion = int(input('Ingrese la opcion(1-5): '))
        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        elif opcion == 2:
            usernameVar = input('Escribe el nombre del usuario: ')
            passwordVar = input('Escribe la contraseña: ')
            usuario = Usuario(username=usernameVar, password=passwordVar)
            usuariosInsertados = UsuarioDAO.insertar(usuario)
            log.info(f'usuarios insertados: {usuariosInsertados}')
        elif opcion == 3:
            idUsuarioVar = int(input('Escribe la id del usuario a modificar: '))
            usernameVar = input('Escribe el nombre del usuario: ')
            passwordVar = input('Escribe la contraseña: ')
            usuario = Usuario(idUsuarioVar, usernameVar, passwordVar)
            usuariosActualizados = UsuarioDAO.actualizar(usuario)
            log.info(f'Usuarios Modificados: {usuariosActualizados}')
        elif opcion == 4:
            idUsuarioVar = int(input('Escribe la id del usuario a eliminar: '))
            usuario = Usuario(idUsuario=idUsuarioVar)
            usuariosEliminados = UsuarioDAO.eliminar(usuario)
            log.info(f'Usuarios Eliminados: {usuariosEliminados}')
        elif opcion != 5:
            log.info('ERROR, OPCION INVALIDA, REINTENTAR..')
    except Exception as e:
        log.info(f'Ocurrio un error: {e}')

else:
    log.info('Fin aplicacion')
