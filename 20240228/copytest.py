# -*- coding: utf-8 -*-
# Auther : jianlong
list1 = [1, 2]
list2 = list1.copy()
list1.append(3)
print(id(list1))
print(id(list2))

list3 = [[1, 2, 3]]
list4 = list3.copy()
list3[0].append(4)
print(id(list3[0]))
print(id(list4[0]))
