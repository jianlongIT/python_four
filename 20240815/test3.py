# -*- coding: utf-8 -*-
# Auther : jianlong
import random

happy = {
    "1": {"name": "富强福", "num": 0},
    "2": {"name": "和谐福", "num": 0},
    "3": {"name": "友善福", "num": 0},
    "4": {"name": "爱国福", "num": 0},
    "5": {"name": "敬业福", "num": 0}
}
print("集五福，迎新春~\n")
while not all(list(map(lambda x: happy[x]['num'], happy))):
    start = input("\r\n按下<Enter>键集五福，迎新春")
    if isinstance(start, str):
        number = random.randint(1, 5)
        str_number = str(number)
        happy[str_number]['num'] += 1
        print('获取到:{}'.format(happy[str_number]['name']))
        print("当前拥有的福:")
        for value in happy.values():
            print('{}{}张 '.format(value['name'], value['num']), end='\t\t')
print('\r\n恭喜集齐五福')
