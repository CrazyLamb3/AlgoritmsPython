# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#неоптимальный по ресурсам алгоритм
#в цикле найти сразу 2 минимальных элемента
import random
from test import sum_memory
lst = [random.randint(-20, 20) for i in range(0, 8)]
print(lst)
if lst[0] > lst[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
for i in range(2, len(lst)):
    if lst[i] < lst[min1]:
        k = min1
        min1 = i
        if lst[k] < lst[min2]:
            min2 = k
    elif lst[i] < lst[min2]:
        min2 = i
print('Два наименьгих числа: {} {}'.format(lst[min1], lst[min2]))
objs = locals().copy()
print(sum_memory(objs))

#OS x64 python 3.7.1
# [20, -1, -1, -7, 14, -18, 9, -8]
# Два наименьгих числа: -18 -8
# переменная lst класса <class 'list'> хранит [20, -1, -1, -7, 14, -18, 9, -8] и занимает 68 байт
# переменная min1 класса <class 'int'> хранит 5 и занимает 14 байт
# переменная min2 класса <class 'int'> хранит 7 и занимает 14 байт
# переменная i класса <class 'int'> хранит 7 и занимает 14 байт
# переменная k класса <class 'int'> хранит 3 и занимает 14 байт
# 124
