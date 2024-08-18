# -*- coding: utf-8 -*-
# Auther : jianlong
import os


def create_pa(path):
    if os.path.exists(path):
        raise Exception('文件已经存在{}'.format(path))
    os.mkdir(path)
    new_path = os.path.join(path, '__init__.py')
    f = open(new_path, 'w')
    f.write('"# coding:utf-8"')
    f.close()


class Open(object):
    def __init__(self, path, mode='w', is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode)
        if self.is_return and not message.endswith('\n'):
            message = '%s\n' % message
        f.write(message)
        f.close()

    def read(self, is_strip=True):
        with open(self.path, mode=self.mode) as f:
            data = f.readlines()
        result = []
        for i in data:
            if is_strip:
                result.append(i.strip())
            else:
                result.append(i)
        return result


if __name__ == '__main__':
    path = os.getcwd() + '/jianlong.txt'
    o = Open(path, mode='r')
    # o.write('succes')
    print(o.read(False))
