# -*- coding: utf-8 -*-
# Auther : jianlong
import random

dict1 = {0: '石头', 1: '剪刀', 2: '布'}
man = random.choice(list(dict1.keys()))
computer = random.choice(list(dict1.keys()))
if computer == man:
    print('人{} 电脑{} 平局'.format(dict1[man], dict1[computer]))
elif (man + 1) % 3 == computer:
    print('人{} 电脑{} 人获得胜利'.format(dict1[man], dict1[computer]))
else:
    print('人{} 电脑{} 电脑获得胜利'.format(dict1[man], dict1[computer]))
