# -*- coding: utf-8 -*-
# Auther : jianlong
num = 0
list1 = []
for i in range(1, 100):
    if i % 3 == 0 and i % 7 == 0:
        continue
    if i % 3 == 0 or i % 7 == 0:
        list1.append(i)
        num += 1
print(num, list1)

# print('\n'.join(['{}*{}={}'.format(x, j, x * j) for x in range(1, 10) for j in range(1, x + 1)]))
print(['{}*{}={}'.format(x, j, x * j) for x in range(1, 10) for j in range(1, x + 1)])
