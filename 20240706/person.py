# -*- coding: utf-8 -*-
# Auther : jianlong
class Person(object):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print('{} 在奔跑'.format(self.name))

    def jump(self):
        print('{} 在跳跃'.format(self.name))

    def work(self):
        self.jump()
        self.run()

    @staticmethod
    def eat():
        print('eat')


jianlong = Person('jianlong1', 12)
jianlong.run()
jianlong.jump()
jianlong.top = 173
print(jianlong.top)
print('----')
jianlong.work()
Person.eat()
