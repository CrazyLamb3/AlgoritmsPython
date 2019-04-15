# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
all_company = []
Company = namedtuple('Company', 'name, q1, q2, q3, q4, profit')
n = int(input('Введите количество компаний'))
total_profit = 0
for i in range(n):
    name = input('Введите название компании')
    q = []
    for j in range(1, 5):
        k = float(input('Введите прибыль за {} квартал'.format(j)))
        q.append(k)
        total_profit += k
    all_company.append(Company(name, *q, sum(q)))
# print(all_company)
average = total_profit/n
#вывод без использования очередей
# for company in all_company:
#     if company.total > average:
#         print('Компания {} заработала больше, чем средний доход по компаниям {}'.format(company.name, average))
#     else:
#         print('Компания {} заработала меньше, чем средний доход по компаниям {}'.format(company.name, average))
for company in all_company:
    if company.profit > average:
        print('Компания {} заработала больше, чем средний доход по компаниям {}'.format(company.name, average))
for company in all_company:
    if company.profit < average:
        print('Компания {} заработала меньше, чем средний доход по компаниям {}'.format(company.name, average))