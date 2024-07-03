import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
try:

    with conexion:
        with conexion.cursor() as cursor:
          #  sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  #sentencia a ejecutar
          #  llavesPrimaras = ((1, 2, 3, 4),)
           # entrada = input('Proporciona los id\'s a buscar (separados por comas): ')
           # llavesPrimarias = (tuple(entrada.split(',')),) #se necesita una tupla de tuplas
           # cursor.execute(sentencia, llavesPrimarias)
           # registros = cursor.fetchall()  #solicitar  los registros de la consulta
           # for registro in registros:
               # print(registro)
          #  sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
          #  valores = (
          #      ('Marcos', 'Cantu', 'Mcantu@gmail.com'),
          #      ('Angel', 'Quintana', 'Aquinta@gmail.com'),
           #     ('Maria', 'Gonzales', 'Mzales@gmail.com')
           # )
           # sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
           # valores = (
            #    ('Juan', 'Perez', 'JPerez@gmail.com', 1),
            #    ('Jimena', 'Gutierrez', 'IGuti@gmail.com', 2)
           # )
           # cursor.executemany(sentencia, valores)
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s '
            entrada = input('Proporciona los id\'s a eliminar (separados por comas): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            #conexion.commit() lo hace solo gracias a usar el with
            registrosActualizados = cursor.rowcount
            print(f'Registros actualizados: {registrosActualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
