import random

def get_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

def print_array(arr):
    print(" ".join(map(str, arr)))


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2 #разбиваем массив
    left_arr = merge_sort(arr[middle:])
    rigth_arr = merge_sort(arr[:middle])

    return merge_array(left_arr, rigth_arr)

def merge_array(left_arr, rigth_arr):
    result = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(rigth_arr):
        if left_arr[i] <= rigth_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(rigth_arr[j])
            j += 1
    result += left_arr[i:]
    result += rigth_arr[j:]
    return result

arr = get_random_array(20)
print_array(arr)
print(merge_sort(arr))
