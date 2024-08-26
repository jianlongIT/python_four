# -*- coding: utf-8 -*-
# Auther : jianlong
import re

if __name__ == '__main__':
    ksf = '康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅'
    # 使用正则表达式匹配所有非"康师傅"的字符串
    result = re.findall(r'(?!康师傅\b)(\b\w+)', ksf)
    print(result)
