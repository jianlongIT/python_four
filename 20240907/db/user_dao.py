# -*- coding: utf-8 -*-
# Auther : jianlong
from mysql_db import pool


class UserDao(object):
    def login(self, username, password):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select count(*) from t_user where user=%s ' \
                  'and %s = aes_decrypt(unhex(password),"jianlong")'
            cursor.excute(sql, (username, password))
            con.commit()
            count = cursor.fetchone()[0]
            return count == 1
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'select tr.role from t_user u left join t_role tr on u.role_id = tr.id'
            'where u.username=%s'
            cursor.excute(sql, (username,))
            con.commit()
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
