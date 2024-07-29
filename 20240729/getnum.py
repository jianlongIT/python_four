# -*- coding: utf-8 -*-
# Auther : jianlong
import threading
import time

# 创建一个锁
lock = threading.Lock()


# 奇数生成器
def print_odd(n):
    for i in range(1, n + 1, 2):
        with lock:  # 加锁，确保同一时间只有一个线程可以执行打印
            print(i)
        time.sleep(0.1)  # 假设打印操作需要一点时间


# 偶数生成器
def print_even(n):
    for i in range(2, n + 1, 2):
        with lock:  # 同样需要加锁
            print(i)
        time.sleep(0.1)


# 创建线程
t1 = threading.Thread(target=print_odd, args=(10,))
t2 = threading.Thread(target=print_even, args=(10,))

# 启动线程
t1.start()
t2.start()

# 等待线程结束
t1.join()
t2.join()
