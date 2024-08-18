# -*- coding: utf-8 -*-
# Auther : jianlong

import threading, random, queue

list_all = list(range(0, 100))
queue_num = queue.Queue(5)


def get_num(thread_name):
    get_list = []
    for i in range(20):
        one = random.choice(list_all)
        list_all.remove(one)
        get_list.append(one)
    print(thread_name, '获得了糖果{}颗'.format(len(get_list)), get_list)
    queue_num.put(get_list)


if __name__ == '__main__':
    t_list = []
    for i in range(5):
        t = threading.Thread(target=get_num, args=('thread_%s' % i,))
        t.start()
        t_list.append(t)
    print('队列结果', queue_num.get())
    print('队列结果', queue_num.get())
    print('队列结果', queue_num.get())
    print('队列结果', queue_num.get())
    print('队列结果', queue_num.get())
