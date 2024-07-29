# -*- coding: utf-8 -*-
# Auther : jianlong
import inspect


def check_str(func):
    def inner(*args, **kwargs):
        if len(args) == 2:
            print('args is ok')
        else:
            return
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is {}'.format(result)
        else:
            return 'result is filed {}'.format(result)

    return inner


@check_str
def test(*data):
    print(inspect.currentframe().f_code.co_name)
    return data


result = test('a', 'b')
print(result)
