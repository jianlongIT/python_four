# -*- coding: utf-8 -*-
# Auther : jianlong
import threading, random
from concurrent.futures import ThreadPoolExecutor

lists = ['一等奖：手机，价值3999元',
         '二等奖：平板电脑，价值1999元',
         '三等奖：加湿器，价值198元']
phones = []
lock = threading.Lock()
for i in range(20):
    phone = str(random.random())[2:13]
    phones.append(phone)


def work():
    lock.acquire()
    if len(lists) > 0:
        one = random.choice(phones)
        phones.remove(one)
        gift = random.choice(lists)
        lists.remove(gift)
        print('手机号为{}的用户抽中了{}'.format(one, gift))
    lock.release()


if __name__ == '__main__':
    print(phones)
    pool = ThreadPoolExecutor(3)
    for i in range(len(lists)):
        pool.submit(work)
