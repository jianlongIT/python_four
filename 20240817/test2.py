# -*- coding: utf-8 -*-
# Auther : jianlong
import multiprocessing, os, time


def work(count, lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(1)
    result = '%s ------------ %s' % (count, os.getpid())
    lock.release()
    return result


if __name__ == '__main__':
    results = []
    pool = multiprocessing.Pool(5)
    lock = multiprocessing.Manager().Lock()
    for i in range(20):
        result = pool.apply_async(func=work, args=(i, lock))
        results.append(result)
    pool.close()
    pool.join()
    for res in results:
        print(res.get(), os.getpid())
