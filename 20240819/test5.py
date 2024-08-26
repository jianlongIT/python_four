# -*- coding: utf-8 -*-
# Auther : jianlong

import asyncio, random

beans = list(range(50))
lock = asyncio.Lock()


async def get_one():
    async with lock:
        if beans:
            one = random.choice(beans)
            beans.remove(one)
            return one
        return None


async def a_get():
    a_beans = []
    while len(beans) > 0:
        a_one = await get_one()
        await asyncio.sleep(random.random())
        a_beans.append(a_one)
    return a_beans


async def b_get():
    b_beans = []
    while len(beans) > 0:
        b_one = await get_one()
        await asyncio.sleep(random.random())
        b_beans.append(b_one)
    return b_beans


async def work():
    result = await asyncio.gather(b_get(), a_get())
    return result


if __name__ == '__main__':
    final_result = asyncio.run(work())
    print(len(final_result[0]), final_result[0], len(final_result[1]), final_result[1])
