# -*- coding: utf-8 -*-
# Auther : jianlong
import threading, random
import time

lists = ['python', 'django', 'tornado',
         'flask', 'bs5', 'requests', 'uvloop']
new_lists = []


def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_lists.append('%s_new' % data)
    time.sleep(5)


if __name__ == '__main__':
    start = time.time()
    t_list = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t.setDaemon(True)
        t.start()
        t_list.append(t)

    print('old_list {}'.format(lists))
    print('new_list {}'.format(new_lists))
    print('use_time {}'.format(time.time() - start))
