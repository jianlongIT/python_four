# -*- coding: utf-8 -*-
# Auther : jianlong
class Cat(object):
    __cat_type = 'cat'

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return '{} {}小猫{}跳着'.format(self.__cat_type, self.name, self.__sex)

    def __run(self):
        return '小猫{}奔跑着'.format(self.name)

    def run(self):
        result = self.__run()
        print(result)


mili = Cat('米粒', '公')
mili.jump()
mili.run()
print(mili._Cat__sex)
