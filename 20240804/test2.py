# -*- coding: utf-8 -*-
# Auther : jianlong

my_list = [1, 2]

def num_add(num):
    length = len(my_list)
    if length == num:
        print(my_list[num - 1])
    else:
        my_list.append(my_list[length - 1] + my_list[length - 2])
        num_add(num)

num_add(30)


def f(n):
    if n < 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(30))
