#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

number = int(input(f'Введи количество элементов массива N -> '))
listNumber = []
for i in range(number):
    listNumber.append(random.randint(1, number))
print(listNumber)

search_number = int(input(f'Введи искомое число Х -> '))

num = listNumber[0]
dif = abs(listNumber[0]-search_number)

for i in listNumber:
    if abs(i-search_number) < dif:
        dif = abs(i-search_number)
        num = i

print(f'Ближайшее число массива к искомому элементу = {num}')
