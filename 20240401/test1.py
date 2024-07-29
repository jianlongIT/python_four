# -*- coding: utf-8 -*-
# Auther : jianlong
dict1 = {'xiaoming': {'name': 'xiaoming', 'age': 12, 'class': 1},
         'xiaohong': {'name': 'xiaohong', 'age': 13, 'class': 1}, }

new_xiaoming = {'xiaoming_new': {'name': 'xiaoming', 'age': 14, 'class': 1}}

if 'xiaoming' in dict1:
    new_xiaoming.update({'xiaoming_new': {'name': 'xiaoming', 'age': 14, 'class': 1}})
    dict1.update(new_xiaoming)
else:
    dict1.update(new_xiaoming)

print(dict1)


