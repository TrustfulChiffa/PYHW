# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве 
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк 
# и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        row_elements = []
        for col in range(1, num_columns + 1):
            row_elements.append(str(operation(row, col)))
        print(" ".join(row_elements))

print_operation_table(lambda x, y: x * y)



# Пытался сделать так, чтобы корректно работали и другие функции (сложение, дление, степень и тд), но без сильного усложнения кода не получается, кажется, будто должно быть
# более изящное решение
# Порылся на stackoverflow, там было вот такое решение:

# from math import log10
# def printOperationTable(operation, numRows=9, numColumns=9):
#     if operation(1,1)==2:
#         print(1,end='\t')
#     colSize = int(log10(operation(numRows+1, numColumns+1)))+2
#     for row in range(1, numRows+1):
#         for column in range(1, numColumns+1):
#             if operation(1,1)==2:
#                 column=column-1
#             print("{:>{}}".format(operation(row,column), colSize), end='\t')
#         print()
# printOperationTable(lambda x,y: x*y, 10, 10)

# Но оно тоже косячит в случае с заменой умножения на другую функцию



# Сложение решается просто изменением нумерации с 1 на 0 для оносительно корректного отображения:

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for row in range(0, num_rows + 1):
#         row_elements = []
#         for col in range(0, num_columns + 1):
#             row_elements.append(str(operation(row, col)))
#         print(" ".join(row_elements))
# print_operation_table(lambda x, y: x + y)

# Но почему-то мне кажется, что тут есть более красивое решение