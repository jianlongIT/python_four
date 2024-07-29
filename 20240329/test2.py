# -*- coding: utf-8 -*-
# Auther : jianlong

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print('{} * {} = {}'.format(i, j, i * j), end=' ')
        if i == j:
            print('\n', end='')
