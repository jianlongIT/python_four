# -*- coding: utf-8 -*-
# Auther : jianlong
list1 = [99, 96, 97.5, 89, 95.5, 93, 99, 95, 98, 99.5]
list1.remove(max(list1))
list1.remove(min(list1))
list1.sort()
print(sum(list1)/len(list1))
