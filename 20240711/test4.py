# -*- coding: utf-8 -*-
# Auther : jianlong
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex


class Bird(Animal):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self.kind = kind


bird = Bird('jianlong', 13, 'ss')
