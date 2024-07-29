# -*- coding: utf-8 -*-
# Auther : jianlong

def demo(i, list1=None):
    if list1 is None:
        list1 = []
    for i in range(i):
        list1.append(i * i)
    return list1


print(demo(3))
print(demo(4))
print(demo(5))
