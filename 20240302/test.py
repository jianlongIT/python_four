# -*- coding: utf-8 -*-
# Auther : jianlong
str = "jianlong"
list1 = []
list1.extend(str)
list1.reverse()
str2 = ''.join(list1)
str3 = str2[::-1]
print(str2)
print(str3)
