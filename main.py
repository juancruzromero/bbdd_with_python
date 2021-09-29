import psycopg2
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLES = """CREATE TABLE users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

if __name__ == '__main__':
    try:
        # connect = psycopg2.Connect(host=config('HOST'),
        #                             port=config('PORT'),
        #                             user=config('USER_MYSQL'),
        #                             passwd=config('PASSWORD_MYSQL'),
        #                             db=config('BD_MYSQL'))

        # Conectarse con Postgres:
        connect = psycopg2.connect("AGREGAR ARGUMENTOS")
        
        with connect.cursor() as cursor: 
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLES)

            query = "INSERT INTO users(username, password, email) VALUES(%s,%s,%s)"
            values = ("juanito","0123456789","tuvieja@ndea.com")

            cursor.execute(query, values)
            connect.commit() # Confirmo persistencia de datos.

            # Obtener registros:
            query = "SELECT * FROM users"
            rows = cursor.execute(query)
            print(rows)
            print(cursor.fetchall())

            # Actualizar registros
            query = "UPDATE users SET username = %s WHERE id=%s"
            vales = ("Cambio de username", 1)
            cursor.execute(query, values)
            connect.commit()

            # Eliminar registro/s
            query = "DELETE FROM users WHERE id=%s"
            cursor.execute(query, (5,))
            connect.commit()

    except psycopg2.OperationalError as err:
        print("no pudo conectarase")
        print(err)
    
    finally:
        connect.close()
        print('Conexión finalizada')