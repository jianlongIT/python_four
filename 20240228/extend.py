# -*- coding: utf-8 -*-
# Auther : jianlong
list1 = [1]
list2 = [2, 3]
list1.extend(list2)
print(list1, list2)

dict1 = {'1': 2}
list1.extend(dict1)
print(list1)

list5 = [1, 3, 7, 9]
list5.extend([2, 2, 6, 8])
list5.sort()
print(list5)
