# -*- coding: utf-8 -*-
# Auther : jianlong
import time, asyncio, threading,gevent


async def a():
    print('a', threading.current_thread().getName())
    return 'func a'


async def b():
    for i in range(10):
        print('b', threading.current_thread().getName())
        await asyncio.sleep(0)

    return 'func b'


async def work():
    result = await asyncio.gather(b(), a())
    print(result[0], result[1])


if __name__ == '__main__':
    asyncio.run(work())
