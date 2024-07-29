# -*- coding: utf-8 -*-
# Auther : jianlong
class Test(object):

    def __init__(self, a):
        self.a = a

    def run_s(self):
        print('run')
        self.jump()

    @classmethod
    def jump(cls):
        print('jump')

    @staticmethod
    def sleep():
        print('i want sleep')


t = Test('a')
t.run_s()
Test.sleep()
t.jump()
t.sleep()