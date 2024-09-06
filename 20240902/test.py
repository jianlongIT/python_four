# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql.connector import connect

if __name__ == '__main__':
    con = connect(host='localhost',
                  port='3306',
                  user='root',
                  password='Jianlong123.',
                  database='vega')
    c = con.cursor()
    sql = 'select * from t_type';
    c.execute(sql)
    print(c.fetchone())
    con.close()
