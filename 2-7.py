 # Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
 # 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
try:
    n = int(input('Введите число n:'))
    s1, i = 0, 1
    s2 = int(n*((n+1)/2))
    while i <= n:
        s1 += i
        i += 1
    if s1 == s2:
        print('Доказано! Суммы равны: {}=={}'.format(s1, s2))
    else:
        print('Недоказано')
except ValueError:
    print('Ввели неверные значения')
