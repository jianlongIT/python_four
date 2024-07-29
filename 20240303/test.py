# -*- coding: utf-8 -*-
# Auther : jianlong
file_path = "F:\imoocProjects\askDemo\imooc\demo.py"
print(file_path[file_path.rfind("\\") + 1:])

grade_one = {
    "class_1": {"boy": 25, "gril": 22},
    "class_2": {"boy": 21, "gril": 23},
    "class_3": {"boy": 24, "gril": 22},
    "class_4": {"boy": 22, "gril": 22},
    "class_5": {"boy": 20, "gril": 25}
}

for i in range(0, 5):
    print('一年{}班: {}'.format(i + 1, list(grade_one.values())[i]))

print(grade_one.get('a'))
