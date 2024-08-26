# -*- coding: utf-8 -*-
# Auther : jianlong
import re

if __name__ == '__main__':
    data = 'jianlong.com'
    result = re.search('\w*', data)
    data1 = result.groups()
    print(data1)

    text = "The price is $100, and the discount price is $80."
    matches = re.findall(r'\$\d+', text)
    print(matches)

    str_1 = 'I don\'t want to be your entire world, just the best thing in it, I want to say "$%^&*@#~!".'
    m = re.findall('\"', str_1)
    print(m)
    str_2 = "12i3 love 34you3 not 56because of 7who3 119  df44"
    m2 = re.findall(r'\d\w*\d', str_2)
    print(m2)
