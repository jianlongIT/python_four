# -*- coding: utf-8 -*-
# Auther :
sum1 = 0
num = 0

while num <= 1000:
    if num % 2 != 0:
        sum1 += num
    num += 1

print(sum1)
list1 = [s * 2 for s in range(20)]
print(type(list1))
s2 = (s * 2 for s in range(20))
print(list(s2))

i = 0
sum = 0

while i <= 100:
    i += 1
    if i % 2 != 0:
        continue
    sum += i
print(sum)

for i in range(1, 10):
    print('')
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(j, i, i * j), end='  ')

print('\n')

a = 1
b = 1
while a <= 9:
    while b < a + 1:
        print('{} * {} = {}'.format(b, a, a * b), end='  ')
        b += 1
    b = 1
    a += 1
    print('')
