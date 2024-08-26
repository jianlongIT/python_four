# -*- coding: utf-8 -*-
# Auther : jianlong
from concurrent.futures import ThreadPoolExecutor
import time, threading, os

lock = threading.Lock()


def work(i):
    return 'work {} {}'.format(i, threading.current_thread().name)


if __name__ == '__main__':
    print('main {}'.format(os.getpid()))
    results = []
    pool = ThreadPoolExecutor(5)
    for i in range(20):
        res = pool.submit(work, (i,))
        results.append(res)
    for r in results:
        print(r.result())
