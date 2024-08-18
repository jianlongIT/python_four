# -*- coding: utf-8 -*-
# Auther : jianlong
import json
import os


def write(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            _data = json.dumps(data)
        else:
            raise TypeError('应该传入字典类型')
        f.write(_data)
    return True


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    return json.loads(data)


path = os.getcwd() + '/test.json'
dict1 = {'name': 'jianlong'}
dict1['sex'] = 'boy'
write(path, dict1)
result = read(path)
print(result)
