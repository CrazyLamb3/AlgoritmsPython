# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
try:
    n = int(input('Введите количество строк матрицы:'))
    k = int(input('Введите количество столбцов матрицы:'))
    m = [[random.randint(0, 20) for j in range(k)] for i in range(n)]
    # print([line for line in m])
    for line in m:
        print(line)
    print(max(list(map(min, zip(*m)))))
except ValueError:
    print('НЕУДАЧНИК')