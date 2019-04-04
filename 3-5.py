# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве:
import random
a = [random.randint(-10, 5) for i in range(0, 30)]
print(a)
maxmin = max([i for i in a if i < 0])
# k = [i for i in range(0, len(a)) if a[i] == maxmin]
print('Максимально отрицательный элемент равен {} с индексами(ом): {}'.format(maxmin, [i for i in range(0, len(a)) if a[i] == maxmin]))