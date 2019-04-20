# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#неоптимальный по ресурсам алгоритм
import random
l = [random.randint(-20, 20) for i in range(0, 8)]
print(l)
print('Два наименьших числа {}'.format([l.pop(l.index(min(l))) for i in range(0, 2)]))
#в цикле найти сразу 2 минимальных элемента
s = [random.randint(-20, 20) for i in range(0, 8)]
print(s)
if s[0] > s[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
for i in range(2, len(s)):
    if s[i] < s[min1]:
        k = min1
        min1 = i
        if s[k] < s[min2]:
            min2 = k
    elif s[i] < s[min2]:
        min2 = i
print('Два наименьгих числа: {} {}'.format(s[min1], s[min2]))

