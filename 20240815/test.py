# -*- coding: utf-8 -*-
# Auther : jianlong
import random

gifts = ['iphone', 'mac', 'ipad']


def gift_ch():
    get_gift = random.choice(gifts)
    print('你得到了%s' % get_gift)


def choice_gift_new():
    gift_num = random.randrange(0, 100, 1)
    if 0 <= gift_num <= 50:
        print('iphone')
    elif 51 <= gift_num <= 70:
        print('mac')
    elif 71 <= gift_num < 100:
        print('mac')


if __name__ == '__main__':
    choice_gift_new()
