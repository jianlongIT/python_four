# -*- coding: utf-8 -*-
# Auther : jianlong
import gevent, time


def work_a():
    for i in range(5):
        print('a - gevent', i)
        gevent.sleep(1)


def work_b():
    for i in range(5):
        print('b - gevent', i)
        gevent.sleep(1)


if __name__ == '__main__':
    start = time.time()
    g_a = gevent.spawn(work_a)
    g_b = gevent.spawn(work_b)
    gevent.joinall([g_a, g_b])
    print(time.time() - start)
