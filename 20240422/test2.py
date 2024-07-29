# -*- coding: utf-8 -*-
# Auther : jianlong

def Recursion(n):
    if n == 1:
        return 1
    else:
        return n * Recursion(n - 1)


f = lambda x, y: x * y
print(f(2, 3))



circle_area = lambda r:3.14 * r * r


print(circle_area(10))