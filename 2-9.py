# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def func9():
    try:
        sum = []
        d = {}
        y = input('Введите натуральные целые числа через пробел:')
        numbers = y.split()
        for i in numbers:
            k, s  = 0, 0
            while k < len(i):
                s += int(i[k])
                k += 1
            sum.append(s)
        m = max(sum)
        d = dict(zip(sum, numbers))
        print('Число {} имеет максимальную сумму {}'.format(d.get(m), m))
    except ValueError:
        print('Ввели неверное значения')
func9()