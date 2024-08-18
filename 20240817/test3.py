# -*- coding: utf-8 -*-
# Auther : jianlong
import multiprocessing, json, time
from multiprocessing import Manager, Pool


class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)
        self.q.put(message)

    def receive(self):
        while True:
            result = self.q.get()
            try:
                res = json.load(result)
            except:
                res = result
            print('result is %s' % res)


if __name__ == '__main__':
    queue = Manager().Queue(5)
    work = Work(queue)
    ws = multiprocessing.Process(target=work.send, args=({'name': 'jianlong'},))
    wr = multiprocessing.Process(target=work.receive)
    ws.start()

    wr.start()
    ws.join()
    wr.terminate()
