# -*- coding: utf-8 -*-
# Auther : jianlong
class Test(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('调用属性函数')
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value


t = Test('jianlong')
t.set_name = 'lalala'
print(t.name)
