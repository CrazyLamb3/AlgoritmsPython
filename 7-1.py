import random

def get_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

def print_array(arr):
    print(" ".join(map(str, arr)))

def bubble_sort(n):
    arr = get_random_array(n)
    print_array(arr)

    for j in range(len(arr)):
        is_sorted = True
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        if is_sorted:
            break

    print_array(arr)

bubble_sort(20)