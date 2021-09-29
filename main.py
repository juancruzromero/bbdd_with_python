import pymysql
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLES = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(host=config('HOST'),
                                    port=config('PORT'),
                                    user=config('USER_MYSQL'),
                                    passwd=config('PASSWORD_MYSQL'),
                                    db=config('BD_MYSQL'))
        
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

    except pymysql.err.OperationalError as err:
        print("no pudo conectarase")
        print(err)
    
    finally:
        connect.close()
        print('Conexión finalizada')