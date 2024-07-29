# -*- coding: utf-8 -*-
# Auther : jianlong
def cap1(data):
    temp = ''
    index = 0
    for x in list(data):
        if index == 0:
            temp = x.upper()
        else:
            temp += x
        index += 1
    return temp


new_str = cap1("sss")
print(new_str)
