# -*- coding: utf-8 -*-
# Auther : jianlong

import schedule
import time


def p(text):
    print(text)


if __name__ == '__main__':
    schedule.every(10).seconds.do(p, 'jianlong')
    while 1:
        schedule.run_pending()
        time.sleep(1)
    print('last')
