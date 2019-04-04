# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
x = input('Введите номер буквы от 1 до 26 из алфавита a-z:')
x = x.lower()
try:
    if len(x) != 1:
       print('Ввели неверное значение!!')
    else:
        line = list('abcdefghijklmnopqrstuvwxyz')
        if not x.isalpha():
            print('Ввели неверные значения')
        elif x in line:
            print((line.index(x)+1))
        else:
            print('Вы ввели неверные значения!!')
except ValueError:
    print('Ввели неверное значение!!')