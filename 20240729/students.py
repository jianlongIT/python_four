# -*- coding: utf-8 -*-
# Auther : jianlong

class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def get_all(self):
        for id_, value in self.students.items():
            print(
                '学号：{}，姓名：{} 年龄：{} 班级：{} 性别：{}'
                    .format(id_, value.get('name'), value.get('age'), value.get('class_number'),
                            value.get('gender')))
        return self.students

    def add(self, **student):
        check = self.check(**student)
        if check is True:
            self.__add(**student)
        else:
            print(check)
            return

    def adds(self, new_students):
        for new_student in new_students:
            check = self.check(**new_student)
            if check is not True:
                print(check, new_student.get('name'))
                continue
            else:
                self.__add(**new_student)

    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print('学号{}不在学生库中'.format(id_))
                continue
            else:
                del_student = self.students.pop(id_)
                print('学号{} 姓名{} 的学生已经被删除'.format(id_, del_student.get('name')))

    def delete(self, student_id):
        if student_id not in self.students:
            print('{} 学号学生信息不存在'.format(student_id))
        else:
            del_stu = self.students.pop(student_id)
            print('{}学号 姓名{}的学生信息已经删除'.format(student_id, del_stu.get('name')))

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在学号为{}的学生'.format(student_id))
        else:
            check = self.check(**kwargs)
            if check is True:
                self.students[student_id] = kwargs
                print('学生信息更新成功')
            else:
                print(check)

    def updates(self, update_students):
        for update_student_id, user_info in update_students.items():
            if update_student_id not in self.students:
                print('并不存在学号为{}的学生'.format(update_student_id))
                continue
            check = self.check(**user_info)
            if check is not True:
                print(check, user_info.get('name'))
                continue
            else:
                self.students[update_student_id] = user_info
        print('所有用户更新完成')

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def search(self, **kwargs):
        search_result = []
        for student in self.students.values():
            flag = True
            for k, v in kwargs.items():
                if isinstance(v, str) and v not in student.get(k):
                    flag = False
                if isinstance(v, int) and v is not student.get(k):
                    flag = False
            if flag:
                search_result.append(student)
        return search_result

    def check(self, **kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有发现学生年龄'
        if 'class_number' not in kwargs:
            return '没有发现学生班级'
        if 'gender' not in kwargs:
            return '没有发现学生性别'
        return True


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

if __name__ == '__main__':
    student_info = StudentInfo(students)
    users = [
        {'name': 'xiaolong',
         'age': 27,
         'class_number': 'B',
         'gender': 'boy'},
        {'name': 'xiaoxiaolong',
         'age': 28,
         'class_number': 'C',
         'gender': 'boy'}
    ]
    student_info.adds(users)

    print(student_info.search(age=28, gender='boy', name='long'))
