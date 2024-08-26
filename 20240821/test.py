# -*- coding: utf-8 -*-
# Auther : jianlong
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list


print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [2]
print(add_item(3))  # 输出: [3]
