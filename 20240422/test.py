# -*- coding: utf-8 -*-
# Auther : jianlong

test_dict = {'a': 1, 'b': 2}


def test1():
    test_dict['c'] = 3


test1()
print(test_dict)

s = (1, 2, 3)
s1 = [1, 2, 3]
s1.append(4)
