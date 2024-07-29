# -*- coding: utf-8 -*-
# Auther : jianlong
list1 = ['苹果']
list1.insert(2, 'sss')
print(list1)
print('{} {} is a list '.format(list1, list1))

list2 = ['a', 'b']
print(id(list2))
print(id(list2))
list2.remove('a')
print(id(list2))

student = ["小花", "小白", "小可", "小糊涂", "小新", "小黑", "小糊涂", "小蓝", "小伟", "小玲", "小撒", "小丽", "小航", "小平", "小圆"]
print(len(student))
print(student.count('小糊涂'))
student.remove('小糊涂')
print(len(student))
print(student.count('小雨'))
student.insert(8, '小雨')
student.append('小刘')
print(len(student))
student.sort(reverse=True)
print(student)
