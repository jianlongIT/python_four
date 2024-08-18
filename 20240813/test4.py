# -*- coding: utf-8 -*-
# Auther : jianlong
import hashlib, time

sign = 'jianlong'


def custom():
    time1 = int(time.time())
    token = '%s%s' % (sign, time1)
    token_en = token.encode('utf-8')
    h_obj = hashlib.sha512(token_en)
    _token = h_obj.hexdigest()
    return _token, time1


def check(_token, timestamp):
    token = '%s%s' % (sign, timestamp)
    token_en = token.encode('utf-8')
    new_token = hashlib.sha512(token_en).hexdigest()
    if new_token == _token:
        return '校验通过，可以帮助'
    else:
        return '校验不通过'


if __name__ == '__main__':
    _token, time1 = custom()
    result = check(_token, int(time.time()))
    print(result)
