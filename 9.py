#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

x = input('Введите три числа через пробел')
a, b, c = x.split()
a, b, c = int(a), int(b), int(c)
if a == b or b == c or a == c:
    print('Вы ввели одинаковые числа')
elif b < a < c or c < a < b:
    print('a =', a)
elif a < b < c or c < b < a:
    print('b =', b)
else:
    print('c =', c)