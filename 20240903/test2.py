# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql.connector import pooling, connect

if __name__ == '__main__':
    try:
        config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'Jianlong123.',
            'database': 'vega'
        }
        pool = pooling.MySQLConnectionPool(**config, pool_size=10)
        con = pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        sql = 'select * from t_user'
        cursor.execute(sql)
        for r in cursor:
            print(r)
        con.commit()
    except Exception as e:
        if 'con' in dir():
            con.roolback()
        print(e)
