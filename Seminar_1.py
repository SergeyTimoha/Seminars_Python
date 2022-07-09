"""Задача 1. Напишите программу, которая принимает на вход два числа и 
проверяет, является ли одно число квадратом другого.
*Примеры:*
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет
"""
# num1 = float(input('Первое число: '))
# num2 = float(input('Второе число: '))
# def funct(a,b):
#     if(a**2==b):
#         return 'Yes'
#     elif(b**2==a):
#         return 'Yes'
#     return 'No'
# print(f"Результат проверки - {funct(num1,num2)}")

# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# ls = list(input('Введите массив - '))

# def max(a):
#     maxnum = a[0]
#     for i in a:
#         if(maxnum<i):
#             maxnum = i
#     return maxnum

# print(f'Результ - {max(ls)}')


# def get_max(a,b,c,d,e):
#     result = max([a,b,c,d,e])
#     return result

# res = get_max(5,25,6,32,5) 
# print(res)


# Задача 4. Напишите программу, которая будет на вход принимать число N и выводить 
# числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def print_number(number):
   for i in range(-number,number+1):
      print(i, end=' ')

n = int(input('Введите число: '))
try:
   n = int(n)
   print_number(n)
except:
    print('Введите целое число: ')


# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать 
# первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# number = float(input('Введите дробное число: '))
# def ferst_num(number):
#     if number % 10 == 0:
#         return 'Нету'
#     else:
#         return int((number * 10)% 10)

# print(f'Первое число от дроби: {ferst_num(number)}')



# Задача 5 . Напишите программу, которая принимает на вход число и проверяет,
#  кратно ли оно 5 и 10 или 15, но не 30.

# num=int(input('Введите число '))
# def krat(a):
#     if ((num % 5 == 0 or num % 10 == 0) or num % 15 == 0) and not (num % 30 == 0):
#         print('da')
#         return num 
#     else:
#         print('net')
# krat(num)

