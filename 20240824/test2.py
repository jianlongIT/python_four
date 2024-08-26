# -*- coding: utf-8 -*-
# Auther : jianlong
import re

if __name__ == '__main__':
    text = '12i3 love 34you3 not 56because of 7who3 119 df44'
    pattern = r'\d\w*\d'

    matches = re.findall(pattern, text)
    print(matches)

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = re.findall(pattern, '328852120@qq..com')
    print(result)
