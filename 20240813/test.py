# -*- coding: utf-8 -*-
# Auther : jianlong

import json

mylist = ['1', '2', '3']
mylist_str = json.dumps(mylist)
print(type(mylist_str))

mylist2 = json.loads('[1,2,3,4]')
print(mylist2)

dict1 = {'name': '鉴龙'}
dict_str = json.dumps(dict1)
dict_obj = json.loads(dict_str)
print(type(dict_obj), dict_obj)

s = (1, 2, 3)
s1 = json.dumps(s)
print(s1)
print(json.loads(s1))

print(json.loads('true'))
