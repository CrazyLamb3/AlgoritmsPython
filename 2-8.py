# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

try:
    number = input('Введите целое число: ')
    numeric = input('Введите цифру, которую необходимо посчитать: ')
    if len(numeric) == 1 and len(number) >= 1 and number.isdigit() and numeric.isdigit():
        k, j = 0, 0
        while k < len(number):
            if numeric == number[k]:
                j += 1
            k += 1
        print('Цифра {} встречается {} раз в числе {}'.format(numeric, j, number))
except ValueError:
    print('Ввели неверные значения')