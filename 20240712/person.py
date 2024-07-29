# -*- coding: utf-8 -*-
# Auther : jianlong
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('hello 我是{}'.format(self.name))

    def relation(self):
        if issubclass(self.__class__, Person):
            print('我的父类是Person')
        else:
            print('父类正在查询中······')


class Student(Person):

    def __init__(self, name, gender, core, major, stu_num='2018014002'):
        super().__init__(name, gender)
        self.core = core
        self.major = major
        self.__stu_num = stu_num

    def speak(self):
        super(Student, self).speak()
        print('我的学号为{} 很高兴认识大家'.format(self.__stu_num))

    def identify_stu(self):
        if self.__stu_num == '2018014002':
            print('我的分组已经完成')
        else:
            print('请稍后，马上为你自动分组')

    def set_num(self, new_num):
        self.__stu_num = new_num


if __name__ == '__main__':
    stu = Student('小明', '男', 'xx', 'xx')
    stu.speak()
    stu.identify_stu()
    stu.relation()
    print('*****')
    stu_2 = Student('小红   ', '女', 'xx', 'xx')
    stu_2.set_num('2018014026')
    stu_2.speak()
    stu_2.identify_stu()
