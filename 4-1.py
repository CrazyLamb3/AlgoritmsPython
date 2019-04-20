# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#неоптимальный по ресурсам алгоритм, а после замеров - алгоритм дернуть элементы быстрее
import random
import timeit
L = [random.randint(-20, 20) for i in range(0, 10000)]
def f1():
    # l = [random.randint(-20, 20) for i in range(0, 8)]
    l = L[:]
    print(l)
    print('Два наименьших числа f1: {}'.format([l.pop(l.index(min(l))) for i in range(0, 2)]))
f1_time = timeit.timeit('f1()', setup='from __main__ import f1', number=100)
def f2():
    #в цикле найти сразу 2 минимальных элемента
    # s = [random.randint(-20, 20) for i in range(0, 8)]
    s = L[:]
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
    print('Два наименьгих числа f2: {} {}'.format(s[min1], s[min2]))
f2_time = timeit.timeit('f2()', setup='from __main__ import f2', number=100)
with open('4-1.txt', 'a', encoding='utf-8') as f:
    f.write(str(f1_time) + '    -    ' + str(f2_time) + '\n')