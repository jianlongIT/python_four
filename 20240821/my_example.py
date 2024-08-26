# -*- coding: utf-8 -*-
# Auther : jianlong

class Student(object):

    def __init__(self, s_number, name, has_class=[]):
        self.s_number = s_number
        self.has_class = has_class
        self.name = name

    def course_detail(self):
        print('Name：{}, Selected：{}'.format(self.name, self.has_class))

    def add_course(self, cour_info):
        self.has_class = []
        self.has_class.append(cour_info)

    def get_msg(self):
        print('name: {},s_number: {}'.format(self.name, self.s_number))


class Teacher(object):

    def __init__(self, t_number, t_name, t_phone):
        self.t_name = t_name
        self.t_number = t_number
        self.t_phone = t_phone

    def get_message(self):
        print('教师编号{} 教师姓名{} 教师手机号{}'.format(self.t_number, self.t_name, self.t_phone))


class Course(object):
    def __init__(self, c_num, c_name, c_teacher=None):
        self.c_num = c_num
        self.c_name = c_name

    def binding(self, teacher):
        self.c_teacher = teacher
        dict_teacher = {}
        if teacher.t_name and teacher.t_number:
            self.c_teacher = teacher
            dict_teacher['课程名称'] = self.c_name
            dict_teacher['教师名称'] = self.c_teacher.t_name
            return dict_teacher
        else:
            return None
