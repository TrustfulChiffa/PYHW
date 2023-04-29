# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if lst[i] >= min_val and lst[i] <= max_val:
            indexes.append(i)
    return indexes

lst = [1, 5, 10, 15, 20, 25]
min_val = 10
max_val = 20
indexes = find_indexes(lst, min_val, max_val)
print(indexes)