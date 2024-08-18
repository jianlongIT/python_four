# -*- coding: utf-8 -*-
# Auther : jianlong
import yaml
import os


def read(path):
    with open(path, 'r') as f:
        data = f.read()
        result = yaml.load(data,Loader=yaml.FullLoader)
    return result


result = read('muke.yaml')
print(result)
