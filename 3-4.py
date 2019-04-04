# 4. Определить, какое число в массиве встречается чаще всего.
import random
import collections
a = [random.randint(0, 20) for i in range(25)]
print(a)
d = dict(collections.Counter(a).most_common(1))
print('Число {} встречается {} раз(а)'.format(list(d.keys()), list(d.values())))