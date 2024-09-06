# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql.connector import pooling

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
        sql = 'insert into t_type(id,type) values(%s,%s)'
        insert_data = [(8, '音乐')]
        cursor.executemany(sql, insert_data)
        result = cursor.fetchall()

        con.commit()
    except Exception as e:
        if 'con' in dir():
            con.rollback()
        print(e)
