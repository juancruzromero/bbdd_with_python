import pymysql
# from config

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    passwd='secret',
                                    db='test')
        print("conectado")
    except pymysql.err.OperationalError as err:
        print("no pudo conectarase")
        print(err)