# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
try:
    n = int(input('Введите  количество элементов'))
    s = 0 # сумма ряда
    i = 0 # счетчик цикла и степень деления
    while i < n:
        s += 1 / (2 ** i)
        i += 1
    print('Сумма {} элементов = {}'.format(n, s))
except ValueError:
    print('Ввели неверные значения')
