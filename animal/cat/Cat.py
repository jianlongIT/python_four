# -*- coding: utf-8 -*-
# Auther : jianlong

class Cat(object):
    def __init__(self, age):
        self.age = age

    def msg(self):
        print('my age is {}'.format(self.age))
