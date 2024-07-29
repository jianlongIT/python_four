# -*- coding: utf-8 -*-
# Auther : jianlong
class Cat(object):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print('我是{} 我今年{}岁 我是{}的'.format(self.name, self.age, self.color))

    def eat(self):
        print('{} 喜欢吃鱼'.format(self.name))

    def catch(self):
        print('{} 能捉老鼠'.format(self.name))


huahua = Cat('花花', 2, '黑色')
huahua.eat()
xueqiu = Cat('雪球', 3, '白色')
xueqiu.catch()
