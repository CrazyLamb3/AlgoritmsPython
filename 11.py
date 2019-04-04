#2. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать.
#После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
#В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”)

import random
try:
    n = int(input('Введите пороговое значения для диапазона получения рандомного числа от 1 до n: '))
    k = int(input('Введите число попыток для угадывания числа от 1 до {}: '.format(n)))
    x = random.randint(1, n)
    print(x)
    while k != 0:
        k -= 1
        y = int(input('Введите число, у вас осталось {} попыток:'.format(k)))
        if y == x:
            print('Вы угадали число')
            break
    else:
        print('Вы не угадали!!!')
except ValueError:
    print('Вы ввели неверные значения')

