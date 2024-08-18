# -*- coding: utf-8 -*-
# Auther : jianlong

def test():
    try:
        raise Exception('报错了')
        return 'ss'
    except Exception as e:
        print(e)
    finally:
        return 'aaa'


result = test()
print(result)
