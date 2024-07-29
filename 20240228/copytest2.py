# -*- coding: utf-8 -*-
# Auther : jianlong
staff_list = [
    ['燕燕', '小洁', '阿楠', '小欣', '辰辰', '小浩'],  # 技术部
    ['小美', '威威', 'Letty', 'Sophia'],  # 测试部
    ['萌萌', '飞飞', '小刚', '佰佰'],  # 产品部
    ['Tom', '小慕'],  # 行政部
    ['铭铭', 'Lily'],  # 财务部
    ['天天', '小晴']  # 人力资源部
]

copy_list = staff_list.copy()
staff_list[2].append('Linda ')
staff_list[0].append('琳琳')
staff_list[0].remove('小洁')
staff_list[0].remove('辰辰')
staff_list[1].remove('Letty')
print(copy_list)
