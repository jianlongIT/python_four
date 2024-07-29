# -*- coding: utf-8 -*-
# Auther : jianlong
import time


def wai(func):
    def inner(*args, **kwargs):
        one_time = time.time()
        result = func(*args, **kwargs)
        sec_time = time.time()
        last_time = sec_time - one_time
        print('耗时{}'.format(last_time))
        return result

    return inner


@wai
def test(name):
    print(name)
    time.sleep(5)



test('jianlong')
