# -*- coding: utf-8 -*-
# Auther : jianlong

students = {
    1: {
        'name': 'jianlong',
        'age': 33,
        'class_number': 'A',
        'gender': 'boy'
    },
    2: {
        'name': 'xiaoguo',
        'age': 28,
        'class_number': 'B',
        'gender': 'boy'
    },
    3: {
        'name': 'xiaoling',
        'age': 28,
        'class_number': 'B',
        'gender': 'girl'
    },
    4: {
        'name': 'xiaoyun',
        'age': 28,
        'class_number': 'B',
        'gender': 'girl'
    },
    5: {
        'name': 'xiaoman',
        'age': 22,
        'class_number': 'A',
        'gender': 'girl'
    }

}


def get_all_students():
    for id_, value in students.items():
        print(
            '学号：{}，姓名：{} 年龄：{} 班级：{} 性别：{}'
                .format(id_, value.get('name'), value.get('age'), value.get('class_number'),
                        value.get('gender')))
    return students


def add_student(**kwargs):
    check = check_student_info(**kwargs)
    if check:
        id_ = max(students) + 1
        students[id_] = kwargs
    else:
        print(check)


def delete_student(student_id):
    if student_id not in students:
        print('{} 学号学生信息不存在'.format(student_id))
    else:
        del_stu = students.pop(student_id)
        print('{}学号 姓名{}的学生信息已经删除'.format(student_id, del_stu.get('name')))


def update_student(student_id, **kwargs):
    if student_id not in students:
        print('并不存在学号为{}的学生'.format(student_id))
    else:
        check = check_student_info(**kwargs)
        if check:
            students[student_id] = kwargs
            print('学生信息更新成功')
        else:
            print(check)


def check_student_info(**kwargs):
    if 'name' not in kwargs:
        return '没有发现学生姓名'
    if 'age' not in kwargs:
        return '没有发现学生年龄'
    if 'class_number' not in kwargs:
        return '没有发现学生班级'
    if 'gender' not in kwargs:
        return '没有发现学生性别'
    return True


def get_student_by_id(student_id):
    return students.get(student_id)


def search_student(**kwargs):
    search_result = []
    for student in students.values():
        flag = True
        for k, v in kwargs.items():
            if student.get(k) != v:
                flag = False
        if flag:
            search_result.append(student)
    return search_result


update_student(1, name='jianlong', age=23, class_number='A', gender='boy')
result = search_student(name='jianlong', age=23)
# add_student(name='lalala', age=17, class_number='A', gender='girl')
# delete_student(1)
# get_all_students()
