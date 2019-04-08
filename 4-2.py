# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без решето Эратосфена
import timeit
def f1():
    # n = int(input('n='))
    n = 10000
    a = []
    for i in range(2, n+1):
        for j in a:
            if i % j == 0:
                break
        else:
            a.append(i)
    return a
def f2():
    # n = int(input('n='))
    n = 10000
    m = [i for i in range(0, n + 1)]
    m[1] = 0
    i = 2
    while i <= n:
        if m[i] != 0:
            j = i + i
            while j <= n:
                m[j] = 0
                j = j + i
        i += 1
    return [i for i in m if i != 0]
# print(f1())
# print(f2())
f1_time = timeit.timeit('f1()', setup='from __main__ import f1', number=100)
f2_time = timeit.timeit('f2()', setup='from __main__ import f2', number=100)
with open('4-2.txt', 'a', encoding='utf-8') as f:
    f.write(str(f1_time) + '    -    ' + str(f2_time) + '\n')
