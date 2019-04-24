# 1. Дан файл  с логинами и паролями. Найдите топ10 самых популярных паролей.
import collections
#берем из файла только пароли
y = []
with open('pwd.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        s = line.strip('\n')
        s = s.split(';')
        if s[1:2] == []:
            continue
        y.append(s[1:2])
#формируем список паролей
z = []
i = 0
while i < len(y):
    z.append(y[i][0])
    i += 1
#получаем 10 самых используемых паролей
c = collections.Counter(z)
d = dict(c.most_common(10))
y = list(d.keys())
k = list(d.values())
print('Топ 10 паролей:')
i, j = 0, 0
while i < len(y):
    print('Пароль {} встречается {} раз(а)'.format(y[i], k[j]))
    i += 1
    j += 1














