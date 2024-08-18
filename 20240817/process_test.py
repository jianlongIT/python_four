# -*- coding: utf-8 -*-
# Auther : jianlong

import time, os, multiprocessing


def work_a():
    for i in range(10):
        if i % 2 == 0:
            print(i, 'a', os.getpid())
            time.sleep(1)


def work_b():
    for i in range(10):
        if not i % 2 == 0:
            print(i, 'b', os.getpid())
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    a_p = multiprocessing.Process(target=work_a)
    b_p = multiprocessing.Process(target=work_b)
    a_p.start()
    b_p.start()
    a_p.join()
    b_p.join()

    print(time.time() - start)
    print('maid pid is %s' % os.getpid())
