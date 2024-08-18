# -*- coding: utf-8 -*-
# Auther : jianlong

list1 = [1, 2, 3, 4]
intr = iter(list1)


def test():
    for i in range(10):
        yield i


t = test()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

res = (i * i for i in range(10))

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

res2 = (i for i in range(10))
print('--------')
for i in res2:
    print(i)