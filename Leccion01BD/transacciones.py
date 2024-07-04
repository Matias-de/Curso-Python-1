import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
'''try:
    conexion.autocommit = False  # no se guardan los cambios hasta que yo no haga commit
    cursor = conexion.cursor()
    #sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    #valores = ('Maria', 'Esparza', 'MSparza@gmail.com')
    #cursor.execute(sentencia, valores)
    sentencia = 'UPDATE persona SET nombre = %s, apellido =%s, email = %s WHERE id_persona = %s'
    valores = ('Roberto', 'Mouras', 'Mmouras@gmail.com', 11)
    cursor.execute(sentencia, valores)
    conexion.commit()  #guardo los cambios, buenas prácticas= hacer esto o usar with
    print('Termina la transaccion, se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback de la transaccion: {e}')
finally:
    conexion.close()'''

# para usar con with:

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'Arojas@gmail.com')
            cursor.execute(sentencia, valores)
            sentencia = 'UPDATE persona SET nombre = %s, apellido =%s, email = %s WHERE id_persona = %s'
            valores = ('Juan', 'Perez', 'JPerez@gmail.com', 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo rollback de la transaccion: {e}')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit')