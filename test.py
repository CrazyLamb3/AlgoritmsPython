import sys

def sum_memory(objs):
    sum_mem = 0
    for item in objs:
        if item.startswith('__'):
            # убираем __
            continue
        elif hasattr(objs[item], '__call__'):
            # убираем функции
            continue
        elif hasattr(objs[item], '__loader__'):
            # убираем модули
            continue
        else:
            sum_mem += sys.getsizeof(objs[item])
            print(f'переменная {item} класса {type(objs[item])} хранит {objs[item]} '
                  f'и занимает {sys.getsizeof(objs[item])} байт')
    return sum_mem


