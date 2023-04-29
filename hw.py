# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def power(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        temp = power(base, exp//2)
        return temp * temp
    else:
        temp = power(base, (exp-1)//2)
        return base * temp * temp

num = int(input("Введите число: "))
power_val = int(input("Введите степень: "))

result = power(num, power_val)

print(f"A = {num}; B = {power_val} -> {result}")
