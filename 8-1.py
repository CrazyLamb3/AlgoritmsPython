# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

def count_hash(s:str):
    set_hash = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            set_hash.add(hash(s[i:j]))
    return len(set_hash) - 1

s = 'mama papa son '
print(count_hash(s))
