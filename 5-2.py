# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
HEX_CONST = 16

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

def sum_hex(a, b):
    a = a.copy()
    b = b.copy()
    if len(b) > len(a):
        a, b = b, a
    b.extendleft('0'*(len(a)-len(b)))
    answer = deque()
    k = 0
    for i in range(len(a) - 1, -1, -1):
        a_num = BIN_NUMBERS[a[i]]
        b_num = BIN_NUMBERS[b[i]]
        number = a_num + b_num + k
        if number >= HEX_CONST:
            k = 1
            number -= HEX_CONST
        else:
            k = 0
        answer.appendleft(HEX_NUMBERS[number])
    if k == 1:
        answer.append('1')
    return answer

def mult_hex(a, b):
    a = a.copy()
    b = b.copy()
    if len(b) > len(a):
        a, b = b, a
    b.extendleft('0'*(len(a)-len(b)))
    answer = deque('0')
    for i in range(len(a) - 1, -1, -1):
        b_num = BIN_NUMBERS[b[i]]
        k = deque('0')
        for j in range(b_num):
            k = sum_hex(k, a)
        k.extend('0'*(len(a) - i - 1))
        answer = sum_hex(answer, k)
    return answer

a = input('Введите первое число')
b = input('Введите второе число')
a = deque(a.upper())
b = deque(b.upper())
print(mult_hex(a,b))
print('Сумма чисел {} и {} равна {}'.format(list(a), list(b), list(sum_hex(a, b))))
print('Произведение чисел {} и {} равно {}'.format(list(a), list(b), list(mult_hex(a, b))))


