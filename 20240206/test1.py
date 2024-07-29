# -*- coding: utf-8 -*-
# Auther : jianlong

str1 = 'jianLONG'
str2 = str1.capitalize()
print(str2)

str3 = 'My name is xiaomu, I\'m from BeiJing';
print(str3.startswith('xiaomu', len('My name is ')))
print(str3.endswith("BeiJing"))

str4 = "ss"
str4 + "a"
print(str4)

str_1 = "小慕买了一本书，58元，一个水杯20元"

str_2 = "一共花了78元"

str_1 = '小慕买了一本书,58元,一个杯子20元'
str_2 = '一共花了78元'

a = '元'
b = '￥.00'

print('my name is %s %c' % ('jianlong', 'S'))
print('my name is {} age is {}'.format('jianlong', 12))
