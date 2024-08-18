# -*- coding: utf-8 -*-
# Auther : jianlong
class MyException(Exception):
    pass


def test(message):
    if message == 'jianlong':
        raise MyException('名字错误')


try:
    assert 1 != 1
except Exception as e:
    print(e)
