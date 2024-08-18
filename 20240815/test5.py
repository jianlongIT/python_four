# -*- coding: utf-8 -*-
# Auther : jianlong
from functools import reduce

frunts = ['apple', 'banana', 'orange']
fil = filter(lambda x: 'e' in x, frunts)
print(list(fil))

list1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, list1)
print(result)

lis2 = ['s', 'sdas', 'ss']
result2 = reduce(lambda x, y: x + y, lis2)
print(result2)

ou = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
filter1 = filter(lambda x: x % 2 == 0, ou)
print(list(filter1))

five = (2, 4, 6, 8, 10, 12)
five = map(lambda x: pow(x, 5), five)
print(list(five))


def use_reduce(number):
    reduce_res = reduce(lambda x, y: x * y, list(range(1, number + 1)))
    return reduce_res


result = use_reduce(20)
print(result)
