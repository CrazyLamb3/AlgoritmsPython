# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
#ищем позиции минимального и максимального элемента
def minmax(a):
    amin, amax = a[0], a[0]
    imax, imin = 0, 0
    for i in range(0, len(a)):
        if amin <= a[i]:
            imin = i
        elif amax >= a[i]:
            imax = i
    print(imax, imin)
    return imax, imin
# a = [random.randint(-20, 20) for i in range(0, 30)]
a = random.sample(range(-20,20),40)
print(a)
imax, imin = minmax(a)
if imin > imax:
    imin, imax = imax, imin
print('Позиции мин и макс элемента: {} {}'.format(imin, imax))
s = [a[i] for i in range(imin+1, imax)]
print('Сумма между элементами {} {} списка равна {}'. format(imin, imax, sum(s)))
#решение используя встроенные функции
# import random
# a = random.sample(range(0, 100), 20)
# print(a)
# xx, yy = a.index(min(a)), a.index(max(a))
# #если максимальный элемент в списке раньше минимального, поменяем индексы местами
# if xx > yy:
#     xx, yy = yy, xx
# s = [a[i] for i in range(xx+1, yy)]
# print('Сумма между элементами {} {} списка равна {}'. format(xx, yy, sum(s)))
