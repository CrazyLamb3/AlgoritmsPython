import random, statistics
m = 4
arr = [random.randrange(0, 100) for _ in range(2 * m + 1)]
print(arr)
print('Медиана = {}'.format(statistics.median(arr)))
print(sorted(arr))