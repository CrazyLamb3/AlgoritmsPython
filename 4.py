# Написать программу, которая генерирует в указанных пользователем границах
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
# надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

x = input('Введите через пробел значения границ:')
try:
    if len(x) < 3:
       print('Ввели неверные значения!!')
    else:
        a, b = x.split()
        line = list('abcdefghijklmnopqrstuvwxyz')
        if a in line and b in line:
            print(line[random.randrange(line.index(a), line.index(b))+1])
        elif type(int(a)) == int and type(int(b)) == int:
            print('Случайное целое число: {}'.format(random.randint(int(a), int(b))))
            print('Случайное вещественное число: {}'.format(round(random.uniform(int(a), int(b)), 3)))
except ValueError:
    print('Ввели неверные значения!!')



