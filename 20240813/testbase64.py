# -*- coding: utf-8 -*-
# Auther : jianlong
import base64

rep_one = '%'
rep_two = '$'


def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(data, bytes):
        data = data
    else:
        raise TypeError('传入类型错误')
    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('a', rep_one).replace('2', rep_two)

    return _data


def decode(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8').replace(rep_one, 'a').replace(rep_two, '2').encode('utf-8')
    if isinstance(data, str):
        data = data.replace(rep_one, 'a').replace(rep_two, '2')
        data = data.encode('utf-8')
    else:
        raise TypeError('类型错误')

    return base64.decodebytes(data).decode('utf-8')


if __name__ == '__main__':
    result = encode('hello jianlong')
    print('result ', result)
    result2 = decode(result)
    print(result2)
