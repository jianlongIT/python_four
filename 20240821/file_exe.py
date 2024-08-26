# -*- coding: utf-8 -*-
# Auther : jianlong

import json, os, random
from my_example import Student, Course, Teacher


def introduction(title):
    print('**********{}**********'.format(title))


def prepare_course():
    courses = []
    with open('course.json', 'r') as f:
        data = f.read()
        data = json.loads(data)
        for i in data.items():
            c = Course(int(i[0]), i[1])
            courses.append(c)
    return courses


def create_teacher():
    teacher_list = []
    old_data = [("T1", "张亮", "13301122001"),
                ("T2", "王朋", "13301122002"),
                ("T3", "李旭", "13301122003"),
                ("T4", "黄国发", "13301122004"),
                ("T5", "周勤", "13301122005"),
                ("T6", "谢富顺", "13301122006"),
                ("T7", "贾教师", "13301122007"),
                ("T8", "杨教师", "13301122008")]
    for one in old_data:
        t = Teacher(one[0], one[1], one[2])
        teacher_list.append(t)
    return teacher_list


def course_to_teacher():
    list_dict_teacher = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()

    for i in range(len(ls_course)):
        dict_teacher = ls_course[i].binding(ls_teacher[i])
        list_dict_teacher.append(dict_teacher)
    return list_dict_teacher


def create_student(c_to_t):
    ls_student = []
    stu = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    for i in range(len(stu)):
        s_number = list(range(1000, 1008))[i]
        student = Student(s_number, stu[i])
        student.add_course(c_to_t[i])
        ls_student.append(student)
    return ls_student


if __name__ == '__main__':
    introduction('学生信息')
    c_to_t = course_to_teacher()
    ls_student = create_student(c_to_t)
    for s in ls_student:
        s.get_msg()
    introduction('选课结果')
    for s in ls_student:
        s.course_detail()
