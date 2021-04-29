# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

num_list = [random.randint(0, 100) for _ in range(10)]
print(*num_list)
spam_min = num_list[0]
spam_max = num_list[1]

for i, item in enumerate(num_list):
    if item <= spam_min:
        spam_min = item
        min_idx = i
    if item >= spam_max:
        spam_max = item
        max_idx = i

num_list[min_idx], num_list[max_idx] = num_list[max_idx], num_list[min_idx]


print('Переставим максимальный и минимальный элементы:\n', *num_list)