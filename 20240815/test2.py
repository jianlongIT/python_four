# -*- coding: utf-8 -*-
# Auther : jianlong
import random

list1 = random.sample(range(1, 33), 6)
list1.append(random.randint(1, 16))
lambda x: str(x).zfill(2), list1
print(list(map(lambda x: str(x).zfill(2), list1)))
