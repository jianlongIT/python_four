# -*- coding: utf-8 -*-
# Auther : jianlong
import copy

huawei_phone = {"P20Pro": 0, "Mate30": 0, "Mate30Pro": 0}
xiaomi_phone = {"mi5s": 0, "mi9pro": 28, "redmi9A": 19}
nokia_phone = {"Lumia920": 0, "nokia_8110": 0}
dict1 = {
    'huawei_phone': {"P20Pro": 0, "Mate30": 0, "Mate30Pro": 0},
    'xiaomi_phone': {"mi5s": 0, "mi9pro": 28, "redmi9A": 19},
    'nokia_phone': {"Lumia920": 0, "nokia_8110": 0}
}
print(dict1.get('xiaomi_phone'))
print(dict1['xiaomi_phone'])

dict1['huawei_phone'].clear()
del dict1['nokia_phone']
print(dict1)
del dict1['xiaomi_phone']['mi5s']
print(dict1)
copy.deepcopy()
