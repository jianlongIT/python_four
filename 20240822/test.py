# -*- coding: utf-8 -*-
# Auther : jianlong
import re

if __name__ == '__main__':
    str_data = 'hegllo jianlong'
    result = re.search('h([a-zA-Z])g', str_data)
    print(result.groups())

    str_data1 = 'jianlong_ 111'
    res1 = re.findall('\Ajia', str_data1)
    print(res1)

    text = "Hello, World!\nThis is a test.\tLet's check spaces."

    # 查找所有的空白字符
    matches = re.findall(r'\s', text)
    print(matches)
