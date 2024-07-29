# -*- coding: utf-8 -*-
# Auther : jianlong
numList = list(range(1, 11))
index = 0
for i in numList:
    if i % 2 == 0:
        index += 1
        print('第 {} 个偶数 {}'.format(index, i))
