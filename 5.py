# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
# между ними находится букв.

x = input('Введите 2 буквы из алфавита a-z:')
try:
    if len(x) < 3:
       print('Ввели неверные значения!!')
    else:
        a, b = x.split()
        a = a.lower()
        b = b.lower()
        line = list('abcdefghijklmnopqrstuvwxyz')
        if not a.isalpha() and not b.isalpha():
            print('Ввели неверные значения')
        elif a in line and b in line and line.index(b) > line.index(a):
            x = line.index(b)-line.index(a)-1 #-1 так как в списке индексы с 0
            print(x)
        else:
            print('Вы ввели неверные значения!!')
except ValueError:
    print('Ввели неверные значения!!')