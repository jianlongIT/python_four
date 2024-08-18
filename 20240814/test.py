# -*- coding: utf-8 -*-
# Auther : jianlong
class Test(object):
    name = 'Jianlong'

    def __init__(self):
        pass


help(Test)
print(vars(Test))
print(dir(Test))
print(hasattr(Test, 'sex'))
print(hasattr(list, 'append'))
