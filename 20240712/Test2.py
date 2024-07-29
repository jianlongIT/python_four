# -*- coding: utf-8 -*-
# Auther : jianlong
class Test2(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __getattr__(self, key):
        print('getattr 内部', key, type(key))

        if self.__attr:
            key = '{}.{}'.format(self.__attr, key)
        return Test2(key)

    def __call__(self, *args, **kwargs):
        print('call', args[0])
        return self


test2 = Test2()
test2('first').a('jianlong').s.c.f.g('second')
