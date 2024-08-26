# -*- coding: utf-8 -*-
# Auther : jianlong

import re

if __name__ == '__main__':
    data1 = 'lianflower@163.com'
    data2 = '11123433@qq.com'
    data3 = 'xinlang@sina.com'
    result1 = re.findall(r'@(.+?)\.', data1)
    print(result1)
    result2 = re.findall(r'@(.+?)\.', data2)
    print(result2)
    result3 = re.findall(r'@(.+?)\.', data3)
    print(result3)

    text = "The rain in Spain falls mainly on the plain."
    result = re.sub(r'\b\w*ain\w*\b', 'sun', text)
    print(result)
