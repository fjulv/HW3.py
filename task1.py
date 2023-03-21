# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

number = int(input(f'Введи количество элементов массива N -> '))
listNumber = []
for i in range(number):
    listNumber.append(random.randint(1, number))
print(listNumber)

search_number = int(input(f'Введи искомое число Х -> '))

count = 0
for j in listNumber:
    if j == search_number:
        count += 1

print(count)